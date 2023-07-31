import boto3
import gcsfs
from PyPDF2 import PdfReader, PdfWriter
from typing import List
from ingestion.document import Document
from io import BytesIO
from ingestion.splitters.text_splitter import RecursiveCharacterTextSplitter


class PyPdfLoader:
    def __init__(self):
        self.reader = PdfReader()
        self.writer = PdfWriter()
        self.streamer = BytesIO()
        self.s3 = boto3.client("s3")
        self.text_splitter = RecursiveCharacterTextSplitter()

    def load(self, file_path) -> List[Document]:
        return self.reader.read(file_path)

    def load_and_split(self, file_path, text_splitter=None) -> List[Document]:
        if text_splitter is None:
            _text_splitter = RecursiveCharacterTextSplitter()
        else:
            _text_splitter = text_splitter
        docs = self.load(file_path)
        return _text_splitter.split_documents(docs)

    def load_metadata(self) -> dict:
        metadata = self.reader.metadata
        if not metadata:
            self.reader.stream.seek(0)
        return metadata

    def read_pdf_stream(self, file_path):
        with open(file_path, "rb") as file_stream:
            return self.reader.read(file_stream)

    def write_pdf_stream(self, file_path) -> bytes:
        with open(file_path, "rb") as file_stream:
            return self.writer.write(file_stream)

    def aws_bucket_reader(self, csv_buffer, bucket_name, file_name):
        # sourcery skip: avoid-builtin-shadow
        object = self.s3.get_object(
            Body=csv_buffer.getValue(), Bucket=bucket_name, Key=f"my/{file_name}.pdf"
        )
        return self.reader(BytesIO(object["Body"].read()))

    def google_bucket_reader(self, project_id, gcs_file_path):
        gcs_file_system = gcsfs.GCSFileSystem(project=project_id)
        gcs_pdf_path = gcs_file_path

        with gcs_file_system.open(gcs_pdf_path, "rb") as f_object:
            reader = self.reader(f_object)
            page_data = {
                page_number: page.__dict__
                for page_number, page in enumerate(reader.pages, start=1)
            }

        return page_data
