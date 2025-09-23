def printer_error(s):
    total_errors = 0
    missprints = 'nñopqrstuvwxyz'
    for item in s:
        if item in missprints:
            total_errors += 1
    return str(total_errors) + '/' + str(len(s))