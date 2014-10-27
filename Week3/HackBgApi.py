import random
import requests


def request(api):
    info = requests.get(api, verify=False)
    data = info.json()
    return data


def list_courses(data):
    all_courses = []
    for student in data:
        for course in student["courses"]:
            if course["name"] not in all_courses:
                all_courses.append(course["name"])
    return all_courses


def match_teams(data, course, team_size, group_time):
    all_students = []
    for student in data:
        for courses in student["courses"]:
            if courses["name"] == course and courses["group"] == group_time:
                all_students.append(student["name"])
    teams = []
    team = []
    random.shuffle(all_students)
    for student in all_students:
        if len(team) < team_size:
            team.append(student)
        elif len(team) == team_size:
            teams.append(team)
            team = []
    return teams


def main():

    data1 = request("https://hackbulgaria.com/api/students/")
    print(list_courses(data1))
    print(match_teams(data1, "Android", 3, 2))


if __name__ == '__main__':
    main()
