import argparse
import yaml
import sys
import queue

#method to load the program arguments
def load_args():
    #Read in command line arguments for the input file
    parser = argparse.ArgumentParser(description='Take in a file containing an experiment schedule and process each job')
    parser.add_argument('schedule', metavar='schedule-file', type=str, nargs='+',
                       help='YAML formatted job scheduler')
    args = parser.parse_args()
    return args.schedule[0]

#method to read the input file and load all jobs into a priority queue
def read_schedule(filename):
    #Create a priority queue for the jobs
    job_q = queue.PriorityQueue()
    try:
        #attempt to open the input file, if you fail, print the exception and exit
        schedule = open(filename, 'r')
        schedule = yaml.load(schedule)
        #attempt to read the input schedule into a dictionary and iterate over it, adding each element to a priority queue
        for k in schedule:
            job_q.put((schedule.get(k).get('Priority'), schedule.get(k)))
    except Exception as e:
        print("Error parsing schedule file: " + str(e))
        sys.exit()
    return job_q

#method to process jobs
def process_jobs(job_q):
    #attempt to run processing logic on all jobs
    while True:
        try:
            job = job_q.get(block=False)
            print("Processing job: " + str(job[1]))
        except:
            print("Job processing completed!");
            break

schedule = load_args()
job_q = read_schedule(schedule)
process_jobs(job_q)
