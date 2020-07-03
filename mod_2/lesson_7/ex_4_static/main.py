from estudent.config import Config
from estudent.school import School


def run_example():
    school = School.create_school_with_students("Hogwart")
    print(school)

    # print(Config.ADMINISTRATOR_EMAIL)
    # print(Config.DATABASE_URL)


if __name__ == '__main__':
    run_example()
