import time
from capmonster_python import HCaptchaTask


class Hcaptcha():
    def __init__(self):
        self.site_key = "03196e24-ce02-40fc-aa86-4d6130e1c97a"
        self.website_url = "https://raffle.bstn.com/"
        self.challange = "river"

    def solve_captcha(self):
        try:
            captcha = HCaptchaTask(client_key="")
            task_id = captcha.create_task(self.website_url, self.site_key)
            print("Starting Solver...")
            start_time = time.time()
            response = captcha.join_task_result(task_id)

            if response != "":
                print("-> hostname = " + self.website_url)
                print("-> site_key = " + self.site_key)
                print("-> challange_type = " + self.challange) 
                print("-> solve_time = " + "%s seconds" % (time.time() - start_time))
            else:
                print("-> Unable to solve captcha")
        except:
            return

solver = Hcaptcha()
solver.solve_captcha()
