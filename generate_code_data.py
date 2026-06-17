import random

# Coding tutorials, GitHub repositories, and API documentation
code_samples = [
    # 1. Python Algorithm (Binary Search)
    {
        "title": "Python Algorithm: Binary Search Implementation",
        "code": """
def binary_search(arr, target):
    \"\"\"
    Searches for a target value within a sorted array.
    Time Complexity: O(log n)
    \"\"\"
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid # target found at index mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 # target not found in array
"""
    },
    
    # 2. PyTorch Neural Network
    {
        "title": "PyTorch: Custom Multi-Layer Perceptron (MLP)",
        "code": """
import torch
import torch.nn as nn

class CustomClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        # Pass input through layers
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out
"""
    },
    
    # 3. Web Dev (HTML/CSS/JS)
    {
        "title": "Web Development: Dynamic Click Counter",
        "code": """
<!DOCTYPE html>
<html>
<head>
    <style>
        .btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <button class="btn" id="counterBtn">Clicks: 0</button>
    <script>
        let count = 0;
        const btn = document.getElementById("counterBtn");
        btn.addEventListener("click", () => {
            count++;
            btn.innerText = `Clicks: ${count}`;
        });
    </script>
</body>
</html>
"""
    },
    
    # 4. Python Algorithm (Bubble Sort)
    {
        "title": "Python Algorithm: Bubble Sort Implementation",
        "code": """
def bubble_sort(arr):
    \"\"\"
    Sorts an array using the bubble sort algorithm.
    Time Complexity: O(n^2)
    \"\"\"
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""
    }
]

def generate_dataset():
    output_path = "input_code.txt"
    dataset_content = ""
    
    # Repeat the coding examples to help the model learn syntactic structures
    for _ in range(350):
        random.shuffle(code_samples)
        for sample in code_samples:
            dataset_content += f"# Document: {sample['title']}\n{sample['code']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset compiled! Code files written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
