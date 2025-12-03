from chainlit.utils import check_module_version

if not check_module_version("langchain", "1.0.0"):
    raise ValueError(
        "Expected LangChain version >= 1.0.0. Run `pip install langchain --upgrade`"
    )
