def main():
    lecture = input('Please talk to me: \n')
    
    lecture_list = lecture.split(' ')

    slow_lecture = '...'.join(lecture_list)

    return slow_lecture


if __name__ == '__main__':
    print(main())