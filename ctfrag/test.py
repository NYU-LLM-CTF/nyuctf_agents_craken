def test_milvus():
    from pymilvus import connections, utility
    connections.connect(
        alias="default",
        host="0.0.0.0",
        port="19530"
    )
    if connections.has_connection("default"):
        print("Connected to Milvus.")
    collections = utility.list_collections()
    print("Current Collections:", collections)
    connections.disconnect("default")

def test_module():
    import sys, os
    from importlib.metadata import distributions
    from pathlib import Path
    TEST_CONTEXT = """
    It seems we don't have permission to install packages. 
    Let's try using Python to interpret the Brainfuck code. I'll create a simple Python script to do this:
    """

    with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
        OPENAI_API_KEY = f.read().strip()
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    # print(sys.modules)
    if "ctfrag" in [dist.metadata['Name'] for dist in distributions()]:
        from ctfrag.rag_agent import RagAgent
        from ctfrag.rag_config import RAGConfig
        agent = RagAgent(config=RAGConfig(config_path=Path(__file__).resolve().parent.parent / "config/rag_config.yaml"))
        response = agent.summarize_context(info=TEST_CONTEXT)
        print(response)
        context, answer = agent.rag_generate(response, collection="writeups")
        print(answer)

if __name__ == "__main__":
    test_module()
