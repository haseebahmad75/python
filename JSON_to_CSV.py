import json

if __name__=="__main__":
    try:
        with open("D:\\data.txt", mode="r") as f:
            data=json.loads(f.read()) # reads a list of dictionaries
        
        output=",".join([*data[0]]) # * unpacks the first dictionary's keys into a list
                                    # write the headers as the first row 
        for item in data: # access each dictionary 
            output+=f"\n{item["id"]},{item["name"]},{item["department"]},{item["semester"]},{item["cgpa"]},{item["city"]}"
        
        with open("converted_data.csv", mode="w") as f:
            f.write(output)
    except Exception as ex:
        print(f"Error: {str(ex)}")
