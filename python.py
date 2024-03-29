from shutil import move, copyfile
import os
import re
import random
import sqlite3
import datetime
from PIL import Image

# from paramiko import SSHClient
from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.internet import reactor
import socket


class NumberWizard:
    """because I'm not g00d @ math."""

    @staticmethod
    def percentage(number, percent):
        return float(number) * float(percent) / 10 ** 2  # yoooo!


class TextWizard:
    """apply massage on strings using coconut oil"""

    @staticmethod
    def reverseString(string):
        """returns reversed string"""
        return string[::-1]

    @staticmethod
    def getFileExtension(file_name):
        """returns file extension of a given file if it exists"""
        if file_name in os.listdir():
            return file_name[::-1].split(".")[0][::-1]  # lol

    # TODO: continue from this function when you come back
    @staticmethod
    def replaceFileExtension(file_path, new_extension):
        tmp = file_path[::-1].split(".")
        extension = TextWizard.reverseString(new_extension)
        tmp[0] = extension
        tmp[0] = tmp[0] + "." + tmp[1]
        del tmp[1]
        tmp = TextWizard.reverseString(tmp)


class Photoshop:
    @staticmethod
    def resize(image_path: str, percent: int):
        """give numbers less than 100 to make smaller and bigger numbers to make it bigger"""

        image = Image.open(image_path)
        new_image_width = int(NumberWizard.percentage(image.width, percent))
        new_image_height = int(NumberWizard.percentage(image.height, percent))
        image = image.resize((new_image_width, new_image_height), Image.ANTIALIAS)
        image.save(image_path)

    @staticmethod
    def convertPng2Jpg(image_path: str):
        if TextWizard.getFileExtension(image_path) == "png":
            image = Image.open(image_path)
            rgb_image = image.convert("RGB")
            rgb_image.save(image_path)

    @staticmethod
    def convertJpg2Png(image_path):
        if TextWizard.getFileExtension(image_path) == "jpg":
            image = Image.open(image_path)
            image.save(image_path)

    @staticmethod
    def bulkConvertPng2Jpg(directory_path):
        """convert all PNG images inside a directory to JPG"""
        for image in os.listdir(directory_path):
            Photoshop.convertPng2Jpg(image)

    @staticmethod
    def bulkConvertJpg2Png(directory_path):
        """convert all JPG images inside a directory to PNG"""
        for image in os.listdir(directory_path):
            Photoshop.convertJpg2Png(image)


class Kindle:
    @staticmethod
    def highlightsToRoam(file):

        # read the content into memory
        org_file = open(file, "r")
        content = org_file.readlines()
        org_file.close()

        # remove carriage returns '^M'
        for line in content:
            line = line.replace("\r", "")

        # remove =======
        for line in content:
            line = line.replace("==========", "")

        # print out content for debugging purposes
        for line in content:
            print(line)

        # write fixed content back
        # org_file = open(file, "w")
        # org_file.write(str(content))
        # org_file.close()

    @staticmethod
    def createLinkFilewise(file, link):
        pass


class Bash:
    """Linux Shell Commands in Python"""

    @staticmethod
    def cp(source_path, destination_path):
        """copies file from source to destinaiton"""
        assert type(source_path) and type(destination_path) is str
        copyfile(source_path, destination_path)

    @staticmethod
    def mv(source_path, destination_path):
        """moves file from source to destinaiton"""
        assert type(source_path) and type(destination_path) is str
        move(source_path, destination_path)

    @staticmethod
    def ls():
        """returns the LIST of items inside the current directory"""
        return os.listdir()

    @staticmethod
    def cd(path):
        """changes directory to the given path"""
        assert type(path) is str, "ERROR: in _cd: path is not string!"
        os.chdir(path)

    @staticmethod
    def pwd():
        """returns current working directory"""
        return os.getcwd()

    @staticmethod
    def touch(file_name):
        """creates a file"""
        assert file_name not in os.listdir(), "Warning! file already exists"
        file = open(file_name, "w")
        file.close()

    @staticmethod
    def cat(file_name):
        """reads and returns the contents of a file"""
        file = open(file_name, "r")
        content = file.readlines()
        file.close()
        return content

    @staticmethod
    def mkdir(directory_name):
        """creates a directory"""
        assert directory_name not in os.listdir(), "Error: directory exists"
        os.mkdir(directory_name)

    @staticmethod
    def grep(regex, file):
        """greps a file just like in linux"""
        matches = []
        _file = open(file, "r")
        for line in _file:
            if re.search(regex, line):
                matches.append(line)
        return matches

    @staticmethod
    def echo(file_name, text):
        """appends some text into a file"""
        file = open(file_name, "a")
        file.write(text)
        file.close()

    @staticmethod
    def rename(file, new_name):
        prefix = os.getcwd() + "/"
        file = prefix + file
        new_name = prefix + new_name
        os.rename(file, new_name)


class Container:
    """List Operations"""

    @staticmethod
    def dump(container):
        """lists entire content of a list"""
        assert type(container) is list
        for element in container:
            print(element)

    @staticmethod
    def sortList(container):
        """sorts the list"""
        return container.sort()

    @staticmethod
    def reverseList(container):
        """revereses all the elements inside a list"""
        assert type(container) is list
        return container.reverse()

    @staticmethod
    def mergeLists(list1, list2):
        """merges given lists together"""
        return list1 + list2

    @staticmethod
    def differrenceOfLists(list1, list2):
        """returns the difference between two lists"""
        return list(set(list1) ^ set(list2))

    @staticmethod
    def stringToList(string):
        """parse words from a string and convert to a list"""
        return string.split(" ")

    @staticmethod
    def listToString(list_of_strings: list):
        """unite all strings inside a list into one string"""
        first_element = list_of_strings[0]
        if type(first_element) == str:
            whole_string = ""
            for string in list_of_strings:
                whole_string += string + " "

            return whole_string


class Random:
    """savolla's custom random library"""

    @staticmethod
    def getRandomInteger(min, max):
        """create a random integer"""
        return random.randint(min, max)

    @staticmethod
    def getListOfRandomIntegers(min, max, amount):
        """generate and return a list of random integers"""
        list_of_randoms = []
        for _ in range(amount):
            list_of_randoms.append(random.randint(min, max))
        return list_of_randoms


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cur = self.connection.cursor()

    def createTable(self, table_name, values):
        query = "CREATE TABLE", table_name
        sub_query = ""
        for i in values:
            sub_query += values[i], " text, "
        # TODO: delete last comma
        # TODO: merget with query
        pass


class Network:
    @staticmethod
    def getMyIP():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip


class Time:
    @staticmethod
    def getCurrentTime():
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @staticmethod
    def getCurrentDate():
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @staticmethod
    def getCurrentWeekDay():
        """returns current day of the week"""
        week_day_names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        week_day_index = datetime.datetime.today().weekday()
        return week_day_names[week_day_index]

    @staticmethod
    def getCurrentMonth():
        pass


# def subtractDates(date1, date2):
#     pass

# FTP
def launchFtpServer():
    reactor.listenTCP(21, FTPFactory(Portal(FTPRealm("./"), [AllowAnonymousAccess()])))
    reactor.run()


# TODO: fix this
class FTPClient:
    pass


# SSH
# TODO: fix this
# def executeCommandThroughSSH(username, ip, password, command):
#     ssh = paramiko.SSHClient()
#     ssh.connect(ip, username=username, password=password)
#     ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
