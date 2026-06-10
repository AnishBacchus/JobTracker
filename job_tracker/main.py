import argparse
from job_tracker.database import init_db, add_application, get_applications
from job_tracker.display import display_applications

def main():
    init_db()

    parser = argparse.ArgumentParser(description="Job Application Tracker")
    subparsers = parser.add_subparsers(dest="command")


    #Add Job to tracker
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--role", required=True)
    add_parser.add_argument("--company", required=True)
    add_parser.add_argument("--application_date")
    add_parser.add_argument("--status", default="Applied")
    add_parser.add_argument("--note")
    


    #Get all jobs from tracker
    list_parser = subparsers.add_parser("all")


    args = parser.parse_args()

    if args.command == "add":
        add_application(args.role, args.company, args.application_date, args.status, args.note)
    elif args.command == "all":
        display_applications(get_applications())


if __name__ == "__main__":
    main()