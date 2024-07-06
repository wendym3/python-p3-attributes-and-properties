APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = APPROVED_JOBS  

    def __init__(self, name="Unknown", job="Admin"):
        self._name = None
        self._job = None
        self.name = name  
        self.job = job  
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name.title()  
        else:
            self._name = None
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in Person.approved_jobs: 
            self._job = job
        else:
            self._job = None
            print("Job must be in list of approved jobs.")
