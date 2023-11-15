import json

with open("input.json") as f:
    json_data = json.load(f)

def task() -> list:


        score = [item["score"] for item in json_data]
        weight = [item["weight"] for item in json_data]
        product = 0
        for i in range(len(score)):
                h = score[i] * weight[i]
                product += h

        return(product)




print(f"{task():.3f}")
