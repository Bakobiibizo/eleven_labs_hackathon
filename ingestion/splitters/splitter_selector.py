from pydantic import BaseModel
from typing import (
    List,
    Optional,
    Any,
    Literal,
    AbstractSet,
    Collection,
    Tuple,
)
from enum import Enum
from ingestion.splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    LatexTextSplitter,
    MarkdownHeaderTextSplitter,
    MarkdownTextSplitter,
    PythonCodeTextSplitter,
    NLTKTextSplitter,
    SpacyTextSplitter,
    TokenTextSplitter,
    SentenceTransformersTokenTextSplitter,
    SentenceTransformersSentenceTextSplitter,
)


class SplittingType(Enum):
    RECURSIVE = "recursive"
    CHARACTER = "character"
    MARKDOWN = "markdown"
    PYTHON = "python"
    NLTK = "nltk"
    SPACY = "spacy"
    TOKEN = "token"
    SENTENCE_TRANSFORMERS = "sentence_transformers"
    LATEX = "latex"


class SplittingReturnType(Enum):
    RECURSIVE = RecursiveCharacterTextSplitter
    CHARACTER = CharacterTextSplitter
    MARKDOWN = MarkdownTextSplitter
    PYTHON = PythonCodeTextSplitter
    NLTK = NLTKTextSplitter
    SPACY = SpacyTextSplitter
    TOKEN = TokenTextSplitter
    SENTENCE_TRANSFORMERS = SentenceTransformersSentenceTextSplitter
    LATEX = LatexTextSplitter


class Pipeline(Enum):
    ENGLISH_CORE: Optional[str] = "en_core_web_sm"
    SENTENCE: Optional[str] = "sentencizer"


class TextSplitterFactory(BaseModel):
    def create_text_splitter(
        self, splitting_type: SplittingType, **kwargs: Any
    ) -> SplittingReturnType:
        if splitting_type == SplittingType.RECURSIVE:
            separators: Optional[List[str]] = kwargs.get("separators", None)
            keep_separators: Optional[bool] = kwargs.get("keep_separator", True)
            self.text_splitter: RecursiveCharacterTextSplitter = (
                RecursiveCharacterTextSplitter(
                    separators=separators, keep_separator=keep_separators, **kwargs
                )
            )
        elif splitting_type == SplittingType.CHARACTER:
            separators: Optional[str] = kwargs.get("separators", "\n\n")
            self.text_splitter: CharacterTextSplitter = CharacterTextSplitter(
                separators=separators, **kwargs
            )
        elif splitting_type == SplittingType.MARKDOWN:
            self.text_splitter: MarkdownTextSplitter = MarkdownTextSplitter(**kwargs)

        elif splitting_type == SplittingType.PYTHON:
            self.text_splitter: PythonCodeTextSplitter = PythonCodeTextSplitter(
                **kwargs
            )
        elif splitting_type == SplittingType.NLTK:
            separators: Optional[str] = kwargs.get("separators", "\n\n")
            self.text_splitter: NLTKTextSplitter = NLTKTextSplitter(
                separators=separators, **kwargs
            )
        elif splitting_type == SplittingType.MARKDOWN_HEADER:
            headers_to_split_on: List[Tuple[str, str]]
            return_each_line: Optional[bool] = kwargs.get("return_each_line", False)
            self.text_splitter: MarkdownHeaderTextSplitter = MarkdownHeaderTextSplitter(
                headers_to_split_on=headers_to_split_on,
                return_each_line=return_each_line,
            )
        elif splitting_type == SplittingType.SPACY:
            separators: Optional[str] = kwargs.get("separators", "\n\n")
            pipeline: Optional[Pipeline] = kwargs.get("pipeline", Pipeline.ENGLISH_CORE)
            self.text_splitter: SpacyTextSplitter = SpacyTextSplitter(
                seperator=separators, pipeline=pipeline, **kwargs
            )
        elif splitting_type == SplittingType.TOKEN:
            encoding_model_name: Optional[str] = kwargs.get(
                "encoding_model_name", "gpt-2"
            )
            model_name: Optional[str] = kwargs.get("model_name", None)
            allowed_special: AbstractSet | Literal["all"] = kwargs.get(
                "allowed_special", set()
            )
            disallowed_special: Collection | Literal["all"] = kwargs.get(
                "disallowed_special", "all"
            )
            self.text_splitter: TokenTextSplitter = TokenTextSplitter(
                encoding_model_name=encoding_model_name,
                model_name=model_name,
                allowed_special=allowed_special,
                disallowed_special=disallowed_special,
                **kwargs,
            )
        elif splitting_type == SplittingType.SENTENCE_TRANSFORMERS:
            chunk_overlap: Optional[int] = kwargs.get("chunk_overlap", 50)
            model_name: Optional[str] = kwargs.get(
                "model_name", "sentence-transformers/all-mpnet-"
            )
            tokens_per_chunk: Optional[int] = kwargs.get("tokens_per_chunk")
            self.text_splitter: SentenceTransformersSentenceTextSplitter = (
                SentenceTransformersTokenTextSplitter(
                    chunk_overlap=chunk_overlap,
                    model_name=model_name,
                    tokens_per_chunk=tokens_per_chunk,
                    **kwargs,
                )
            )

        elif splitting_type == SplittingType.LATEX:
            self.text_splitter: LatexTextSplitter = LatexTextSplitter(**kwargs)
        else:
            raise ValueError("Invalid splitting type specified.")

        return self.text_splitter


class SplitterSelector(TextSplitterFactory):
    def __init__(self, splitter=None):
        super().__init__()
        splitter = splitter
        if splitter is None:
            self.create_text_spliter(splitting_type=splitter)

    def create_character_splitter(self, **kwargs):
        return CharacterTextSplitter(**kwargs)

    def create_markdown_splitter(self, **kwargs):
        return MarkdownTextSplitter(**kwargs)

    def create_python_splitter(self, **kwargs):
        return PythonCodeTextSplitter(**kwargs)

    def create_nltk_splitter(self, separators, **kwargs):
        return NLTKTextSplitter(separators=separators, **kwargs)

    def create_markdown_header_splitter(self, headers_to_split_on, return_each_line):
        return MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on, return_each_line=return_each_line
        )

    def create_spacy_splitter(self, separators, pipeline, **kwargs):
        return SpacyTextSplitter(separators=separators, pipeline=pipeline, **kwargs)

    def create_token_splitter(
        self,
        encoding_model_name,
        model_name,
        allowed_special,
        disallowed_special,
        **kwargs
    ):
        return TokenTextSplitter(
            encoding_model_name=encoding_model_name,
            model_name=model_name,
            allowed_special=allowed_special,
            disallowed_special=disallowed_special,
            **kwargs,
        )

    def create_sentence_transformers_text_splitter(
        self, chunk_overlap, model_name, tokens_per_chunk, **kwargs
    ):
        return SentenceTransformersSentenceTextSplitter(
            chunk_overlap=chunk_overlap,
            model_name=model_name,
            tokens_per_chunk=tokens_per_chunk,
            **kwargs,
        )

    def create_latex_splitter(self, **kwargs):
        return LatexTextSplitter(**kwargs)


def test():
    splitters = TextSplitterFactory()
    splitter_list = SplittingType
    for splitter in splitter_list:
        splitter = splitters.create_text_splitter(splitting_type=splitter)
        print(splitter)


if __name__ == "__main__":
    test()
