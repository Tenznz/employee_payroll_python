class CompanyEmployeeWage:
    # def __int__(self):
    #     pass

    def __init__(self):
        self.company_name = ""
        self.num_of_working_days = 0
        self.max_hrs_in_month = 0
        self.emp_rate_per_hour = 0
        self.total_wage = 0

    def get_company_name(self):
        return self.company_name

    def set_company_name(self, company_name):
        self.company_name = company_name

    def get_num_of_working_days(self):
        return self.num_of_working_days

    def set_num_of_working_days(self, num_of_working_days):
        self.num_of_working_days = num_of_working_days

    def get_max_hrs_in_month(self):
        return self.max_hrs_in_month

    def set_max_hrs_in_month(self, max_hrs_in_month):
        self.max_hrs_in_month = max_hrs_in_month

    def get_emp_rate_per_hour(self):
        return self.emp_rate_per_hour

    def set_emp_rate_per_hour(self, emp_rate_per_hour):
        self.emp_rate_per_hour = emp_rate_per_hour

    def get_total_wage(self):
        return self.total_wage

    def set_total_wage(self, total):
        self.total_wage = total

    def tostring(self):
        pass
