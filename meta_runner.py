import yaml
import os

BASE = "meta_мозг"

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run():
    entry = load_yaml(f"{BASE}/runtime_entry.yaml")

    start_node = entry["execution"]["start_node"]

    print(f"🚀 START from: {start_node}")

    node_path = f"{BASE}/nodes/{start_node}.yaml"

    if not os.path.exists(node_path):
        print("❌ Node not found")
        return

    node = load_yaml(node_path)

    print("🧠 NODE CONTENT:")
    print(node)

    print("\n⚡ Execution simulated")

if __name__ == "__main__":
    run()
