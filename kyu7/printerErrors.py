def printer_error(s):
    total_errors = 0
    missprints = 'nñopqrstuvwxyz'
    for print in s:
        if print in missprints:
            total_errors += 1
    return str(total_errors) + '/' + str(len(s))