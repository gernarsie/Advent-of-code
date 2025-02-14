import pandas as pd

df: pd.DataFrame = pd.read_csv(r"./2024/01/input.txt", names = ["Group 1", "Group 2"], sep = r"\s+")

for col in df.columns:
    df[col] = sorted(df[col])

# Problem 1:
df["Distance"] = abs(df["Group 1"] - df["Group 2"])

total_distance: int = df["Distance"].sum()  

# Problem 2:
df["Similarity"] = df["Group 1"].apply(lambda x: x * df["Group 2"].value_counts().get(x,0))

similarity_score: int = df["Similarity"].sum()


def main() -> None: 
    print(f"Total distance: {total_distance}") # Problem 1
    print(f"Similarity score: {similarity_score}") # Problem 2

if __name__ == "__main__":
    main()