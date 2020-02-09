from Code.code import Code
from MLD.mld import Incomplete, Complete
from Table.table import MLDTable

if __name__ == '__main__':
    
    while(True):
        welcome_message = """
        Welcome to MLD Table Generator, please select an option:

            1. Generate Tx and Rx automatically
            2. Enter Tx code manually
            3. Enter Tx and Rx code manually
            4. Exit
        """

        menu_option = input(welcome_message)

        if int(menu_option) > 3 or int(menu_option) < 1:
            break
        
        first_prob = -1.0
        second_prob = -1.0

        while first_prob < 0.0 or first_prob > 1.0:
            first_prob = float(input('Please Enter P(0 Rx|0 Tx) = '))
        
        while second_prob < 0.0 or second_prob > 1.0:
            second_prob = float(input('Please Enter P(1 Rx|1 Tx) = '))
        
        n = int(input('Please Select n = '))
        
        m = 0
        while m <= 0 or m > 2**n:
            m = int(input('Please enter m (No larger than ' + str(2**n) + '): '))

        message = """
        Select the MLD of your preference:
            1. Complete
            2. Incomplete
            """
        mld_type = input(message)

        probs = [first_prob, second_prob]
        

        if menu_option == '1':
            if mld_type == '1':
                code_tx = Code(n, m)
                code_tx.randomly_fill_set()
                code_rx = code_tx.get_all_posibilities()
                c_mld = Complete((code_tx, code_rx), probs)

                table = MLDTable(c_mld)
                print("\n")
                print('============ Probabilities Table ====================' + '\n')
                table.probs_table()
                print("\n")
                print('============ Complete MLD Table ====================' + '\n')
                table.complete_table()
            
            elif mld_type == '2':
                code_tx = Code(n, m)
                code_tx.randomly_fill_set()
                code_rx = code_tx.get_all_posibilities()
                i_mld = Incomplete((code_tx, code_rx), probs)

                table = MLDTable(i_mld)
                print("\n")
                print('============ Probabilities Table ====================' + '\n')
                table.probs_table()
                print("\n")
                print('============ Incomplete MLD Table ====================' + '\n')
                table.incomplete_table()

        elif menu_option == '2':
            code_set_ = []
            for i in range(0, m):
                codeword = ''
                while len(codeword) != n:
                    codeword = input('Type Tx codeword ' + str(i + 1) + '/' + str(m) + ': ')
                code_set_ += [codeword]

            if mld_type == '1':
                code_tx = Code(n, m, code_set=code_set_)
                code_rx = code_tx.get_all_posibilities()
                c_mld = Complete((code_tx, code_rx), probs)

                table = MLDTable(c_mld)
                print("\n")
                print('============ Probabilities Table ====================' + '\n')
                table.probs_table()
                print("\n")
                print('============ Complete MLD Table ====================' + '\n')
                table.complete_table()
            
            elif mld_type == '2':
                code_tx = Code(n, m, code_set=code_set_)
                code_rx = code_tx.get_all_posibilities()
                i_mld = Incomplete((code_tx, code_rx), probs)

                table = MLDTable(i_mld)
                print("\n")
                print('============ Probabilities Table ====================' + '\n')
                table.probs_table()
                print("\n")
                print('============ Incomplete MLD Table ====================' + '\n')
                table.incomplete_table()
            
        elif menu_option == '3':
            tx_code_set_ = []
            rx_code_set_ = []
            tx_m = m

            for i in range(0, tx_m):
                codeword = ''
                while len(codeword) != n:
                    codeword = input('Type Tx codeword ' + str(i + 1) + '/' + str(tx_m) + ': ')
                tx_code_set_ += [codeword]

            rx_m = 0
            while rx_m <= 0 or rx_m > 2**n:
                rx_m = int(input('\t Please enter Rx_m (No larger than ' + str(2**n) + '): '))

            for i in range(0, rx_m):
                codeword = ''
                while len(codeword) != n:
                    codeword = input('Type Rx codeword ' + str(i + 1) + '/' + str(rx_m) + ': ')
                rx_code_set_ += [codeword]
            

            if mld_type == '1':
                code_tx = Code(n, tx_m, code_set=tx_code_set_)
                code_rx = Code(n, rx_m, code_set=rx_code_set_)
                c_mld = Complete((code_tx, code_rx), probs)

                table = MLDTable(c_mld)
                print("\n")
                print('============ Probabilities Table ====================' + '\n')
                table.probs_table()
                print("\n")
                print('============ Complete MLD Table ====================' + '\n')
                table.complete_table()
            
            elif mld_type == '2':
                code_tx = Code(n, tx_m, code_set=tx_code_set_)
                code_rx = Code(n, rx_m, code_set=rx_code_set_)
                i_mld = Incomplete((code_tx, code_rx), probs)

                table = MLDTable(i_mld)
                print("\n")
                print('============ Probabilities Table ====================' + '\n')
                table.probs_table()
                print("\n")
                print('============ Incomplete MLD Table ====================' + '\n')
                table.incomplete_table()

