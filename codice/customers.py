import numpy as np
import pandas as pd
from pandas import DataFrame
import time 
from tqdm import tqdm

class Customer:
    dataset: DataFrame
    gen_time: float

    def __init__(self, gen, n_customers=0, path=""):
        if gen:
            self.generate_profiles_table(n_customers, 0)
        else:
            self.dataset = pd.read_pickle(path)


    def generate_profiles_table(self, n_customers, random_state=0):
        self.gen_time = time.time()
        np.random.seed(random_state) 
        customer_id_properties=[]
        # Generate customer properties from random distributions 
        for customer_id in tqdm(range(n_customers)):
            x_customer_id = np.random.uniform(0,100)
            y_customer_id = np.random.uniform(0,100)
            mean_amount = np.random.uniform(5,100) # Arbitrary (but sensible) value 
            std_amount = mean_amount/2 # Arbitrary (but sensible) value
            
            mean_nb_tx_per_day = np.random.uniform(0,4) # Arbitrary (but sensible) value 
            
            customer_id_properties.append([customer_id,
                                        x_customer_id, y_customer_id,
                                        mean_amount, std_amount,
                                        mean_nb_tx_per_day])
            
        self.dataset = pd.DataFrame(customer_id_properties, columns=['CUSTOMER_ID',
                                                                        'x_customer_id', 'y_customer_id',
                                                                        'mean_amount', 'std_amount',
                                                                        'mean_nb_tx_per_day'])

        self.gen_time = time.time()-self.gen_time
         
    def get_dataset(self):
        print(self.dataset)
    

    