import logging


def fibinaci(input_list):
    next_entry = input_list[-2] + input_list [-1]
    input_list.append(next_entry)
    logging.info("This iteration is {}".format(input_list))
    if next_entry <= 100:
        fibinaci(input_list)
    else:
        logging.warning("This is the last iteration")
        

if __name__ == "__main__":
    #tell the logging module to print logging.info:
    logging.basicConfig(level = logging.INFO)
    logging.error("error")
    #keep writing to the same file:
    #logging.basicConfig(filename = "example.log", level = logging.INFO)
    #write to a new file every time:
    #logging.basicConfig(filename = "example.log", filemode="w", level = logging.INFO)
    starting_list = [0, 1]
    fibinaci(starting_list)