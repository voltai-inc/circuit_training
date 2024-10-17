import re


def remove_duplicate_nodes(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    nodes = []
    current_node = []
    inside_node = False
    brace_count = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("node {"):
            inside_node = True
            brace_count = 1
            current_node = [line]
            continue
        if inside_node:
            current_node.append(line)
            brace_count += line.count("{")
            brace_count -= line.count("}")
            if brace_count == 0:
                nodes.append("".join(current_node))
                inside_node = False
            continue
        else:
            # Lines outside node blocks are kept as-is
            nodes.append(line)

    seen_names = set()
    unique_nodes = []

    # Regex pattern to extract the name field
    node_pattern = re.compile(r'name\s*:\s*"([^"]+)"')

    for node in nodes:
        if node.startswith("node {"):
            match = node_pattern.search(node)
            if match:
                name = match.group(1)
                if name not in seen_names:
                    seen_names.add(name)
                    unique_nodes.append(node)
                else:
                    # Duplicate node found; skip it
                    print(f"Duplicate node '{name}' found. Skipping.")
            else:
                # No name field found; decide whether to keep or skip
                print("No 'name' field found in a node. Keeping it by default.")
                unique_nodes.append(node)
        else:
            # Non-node lines are kept as-is
            unique_nodes.append(node)

    with open(output_file, "w") as f:
        f.writelines(unique_nodes)

    print(f"Processing complete. Unique nodes have been written to '{output_file}'.")


if __name__ == "__main__":
    remove_duplicate_nodes("data/adaptec1.pb.txt", "data/adaptec1_new.pb.txt")
