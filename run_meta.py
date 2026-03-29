import yaml
import os

ENTRY_PATH = "мета_мозг/runtime_entry.yaml"
NODE_BASE = "meta_brain/узлы/meta_brain/узлы"


def load_yaml(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run():
    if not os.path.exists(ENTRY_PATH):
        print(f"❌ Entry file not found: {ENTRY_PATH}")
        return

    entry = load_yaml(ENTRY_PATH)

    start_node = entry["execution"]["start_node"]
    print(f"🚀 START from: {start_node}")

    node_path = f"{NODE_BASE}/{start_node}.yaml"

    if not os.path.exists(node_path):
        print(f"❌ Node not found: {node_path}")
        return

    node = load_yaml(node_path)

    print("🧠 NODE LOADED")
    print(f"type: {node.get('type')}")
    print(f"status: {node.get('status')}")
    print(f"node_id: {node.get('node_id')}")
    print(f"content: {node.get('content')}")

    print("\n✅ Runtime check passed")


if __name__ == "__main__":
    run()
