import threading
import schedule
import time


class Scheduler:
    def __init__(self, app):
        self.app = app
        self.start()

    def start(self):
        print("Starting scheduler")
        jobs_thread = threading.Thread(target=self.schedule)
        jobs_thread.start()

    # Funzione per eseguire i tuoi job schedulati
    def schedule(self):
        # Esempio di un job schedulato che viene eseguito ogni 5 secondi
        schedule.every(5).seconds.do(self.job)

        # Ciclo per eseguire i job schedulati
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Definisci i tuoi job schedulati qui utilizzando il modulo 'schedule'
    def job(self):
        print('B---------')
        #pprint.pprint(self.app)
        print('----------')

        print("....")
        # pprint.pprint(dir(cheshire_cat_api.state))
        print("Eseguendo un job schedulato...")
