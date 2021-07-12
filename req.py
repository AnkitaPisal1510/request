import requests
import json 
import os 
if os.path.isfile("data1.json"):
    with open("data1.json","r") as data:
        data_1=json.load(data)
else:
    first_api= requests.get("http://saral.navgurukul.org/api/courses")
    data_1 = first_api.json()
    with open("data.json","w") as f:
        json.dump(data_1,f,indent=4)
# giving loop for printing main all topic names
serial_no=1
id_list=[]
for index1 in data_1["availableCourses"]:
    print(serial_no,index1["name"])
    id_list.append(index1["id"])
    serial_no+=1
# giving user input it will print topic name that you want
user1=int(input("enter the topic serial number that you want"))
print(data_1["availableCourses"][user1-1]["name"])
id_=data_1["availableCourses"][user1-1]["id"]
id=id_list[user1-1]
if os.path.isfile("data2"+id+".json"):
    with open("data2"+id+".json","r") as data1:
        data_2=json.load(data1)
else:
    id_=data_1["availableCourses"][user1-1]["id"]
    second_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercises")
    data_2=second_api.json()
    with open("data2"+id+".json","w") as f:
        json.dump(data_2,f,indent=4)

serial_no1=1
for index2 in data_2["data"]:
    print(serial_no1,index2["name"])
    serial_no1+=1
user_input_2=input(" do you wnt to previous or next (n or p):-")
if user_input_2=="p":
    serial_no=1
    for index1 in data_1["availableCourses"]:
        print(serial_no,index1["name"])
        serial_no+=1
    # giving user input it will print topic name that you want
    user_input_3=int(input("enter the topic serial number that you want"))
    print(data_1["availableCourses"][user_input_3-1]["name"])
    # id_=data_1["availableCourses"][user_input_3-1]["id"]
    # passing second api
    if os.path.isfile("data2"+id+".json","r"):
        with open("data2"+id+".json","r") as data1:
            data_2=json.load(data1)
    else:
        id_=data_1["availableCourses"][user_input_3-1]["id"]
        second_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercises")
        data_2=second_api.json()
        with open("data2"+id+".json","w") as f:
            json.dump(data_2,f,indent=4)

    serial_no1=1
    for index2 in data_2["data"]:
        print(serial_no1,index2["name"])
        serial_no1+=1
        serial_no_1=1
        if index2["childExercises"]==[]:
                print("   ",serial_no_1,index2["name"])
                # print(" ",serial_no_1,index2["slug"])
        else:
            serial_no_1_=1
            for index3 in index2["childExercises"]:
                print("    ",serial_no_1_,index3["name"])
                serial_no_1_+=1
    slug1=int(input("enter the point which you want:-"))
        # print(data_2["data"][slug1-1]["childExercises"])
    w=data_2["data"][slug1-1]["slug"]
    slug1_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w)
    slug1_api_json=slug1_api.json()
    with open ("slug1.json","r+") as file3:
        json.dump(slug1_api_json,file3,indent=2)
    s_no=1
    question_list=[]
    for index1 in data_2["data"][slug1-1]["childExercises"]:
        print("           ",s_no,".",index1["name"])
        question_list.append(index1["name"])
        s_no+=1

    que=int(input("Enter question number:"))
    w1=data_2["data"][slug1-1]["childExercises"][que-1]["slug"]
    slug2_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w1)
    slug2_api_json=slug2_api.json()
    with open("question.json","w") as file4:
        json.dump(slug2_api_json,file4,indent=4)
        print(slug2_api_json["content"])

    for index4 in range(len(question_list)):
        user_input_4=input("Enter whether you want to go next or previous(n/p):")
        if user_input_4=="n":
            if que==len(question_list): 
                print("Next page:")
                break
            else:
                w2=(data_2["data"][slug1-1]["childExercises"][que]["slug"])
                slug2_api2_=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w2)
                slug2_api2_json=slug2_api2_.json()
                with open("question.json","w") as file5:
                    json.dump(slug2_api2_json,file5,indent=4)
                    print(slug2_api2_json["content"])
                    que=que+1
        
        if user_input_4=="p":
            if que==len(question_list):
                print("No more questions")
                break
            else:
                w4=data_2["data"][slug1-1]["childExercises"][que-1]["slug"]
                slug2_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w4)
                slug2_api_json=slug2_api.json()
                with open("question.json","w") as file4:
                    json.dump(slug2_api_json,file4,indent=4)
                    print(slug2_api_json["content"])
                    que=que-1
    else:
        slug_list=[]
        s_no=1
        print("     ",slug1,".",[slug1-1])
        print("           ",s_no,".",data_2["data"][slug1-1]["slug"])
        slug_list.append(data_2["data"][slug1-1]["slug"])
        que=int(input("Enter question number:"))
        last_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+str(data_2["data"][slug1-1]["slug"]))
        last_data=last_api.json()
        with open("questions.json","w") as file5:
            json.dump(last_data,file5,indent=4)
            print(last_data["content"])
        for i in range(len(slug_list)):
            user_input_5=input("Enter whether you want to go next or previous:(n/p)")
            if user_input_5=="n":
                print("Next page.")
                break
            else:
                print("No more questions.")
                break
elif user_input_2=="n":
    serial_no1=1
    for index2 in data_2["data"]:
        print(serial_no1,index2["name"])
        serial_no1+=1
        serial_no_1=1
        if index2["childExercises"]==[]:
            print("   ",serial_no_1,index2["name"])
            # print(" ",serial_no_1,index2["slug"])
        else:
            serial_no_1_=1
            for index3 in index2["childExercises"]:
                print("    ",serial_no_1_,index3["name"])
                serial_no_1_+=1
    slug1=int(input("enter the point which you want:-"))
    # print(data_2["data"][slug1-1]["childExercises"])
    w=data_2["data"][slug1-1]["slug"]
    slug1_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w)
    slug1_api_json=slug1_api.json()
    with open ("slug1.json","r+") as file3:
        json.dump(slug1_api_json,file3,indent=2)
    s_no=1
    question_list=[]
    for index1 in data_2["data"][slug1-1]["childExercises"]:
        print("           ",s_no,".",index1["name"])
        question_list.append(index1["name"])
        s_no+=1

    que=int(input("Enter question number:"))
    w1=data_2["data"][slug1-1]["childExercises"][que-1]["slug"]
    slug2_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w1)
    slug2_api_json=slug2_api.json()
    with open("question.json","w") as file4:
        json.dump(slug2_api_json,file4,indent=4)
        print(slug2_api_json["content"])

for index4 in range(len(question_list)):
    user_input_4=input("Enter whether you want to go next or previous(n/p):")
    if user_input_4=="n":
        if que==len(question_list): 
            print("Next page:")
            break
        else:
            w2=(data_2["data"][slug1-1]["childExercises"][que]["slug"])
            slug2_api2_=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w2)
            slug2_api2_json=slug2_api2_.json()
            with open("question.json","w") as file5:
                json.dump(slug2_api2_json,file5,indent=4)
                print(slug2_api2_json["content"])
                que=que+1
    
    if user_input_4=="p":
        if que==len(question_list):
            print("No more questions")
            break
        else:
            w4=data_2["data"][slug1-1]["childExercises"][que-1]["slug"]
            slug2_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+w4)
            slug2_api_json=slug2_api.json()
            with open("question.json","w") as file4:
                json.dump(slug2_api_json,file4,indent=4)
                print(slug2_api_json["content"])
                que=que-1
else:
    slug_list=[]
    s_no=1
    print("     ",slug1,".",[slug1-1])
    print("           ",s_no,".",data_2["data"][slug1-1]["slug"])
    slug_list.append(data_2["data"][slug1-1]["slug"])
    que=int(input("Enter question number:"))
    last_api=requests.get("http://saral.navgurukul.org/api/courses/"+id_+"/exercise/getBySlug?slug="+str(data_2["data"][slug1-1]["slug"]))
    last_data=last_api.json()
    with open("questions.json","w") as file5:
        json.dump(last_data,file5,indent=4)
        print(last_data["content"])
    for i in range(len(slug_list)):
        user_input_5=input("Enter whether you want to go next or previous:(n/p)")
        if user_input_5=="n":
            print("Next page.")
            break
        else:
            print("No more questions.")
            break