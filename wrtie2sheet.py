from pynput import keyboard
import time
import decimal
import xlsxwriter
import Login as lo
def write2sheet(a2, tim2, pr2, rl2, prt2, rlt2, hold2, flight2, master2, ngram2):
    a = a2
    tim = tim2
    pr = pr2
    rl = rl2
    prt = prt2
    rlt = rlt2
    hold = hold2
    flight = flight2
    master = master2
    ngram = ngram2
    if(len(prt) is len(rlt)):
        i = 0
        while i < len(prt):
            if(i>=len(rlt)):
                break
            hold.append(decimal.Decimal(rlt[i]-prt[i]))
            i+=1

        i = 1
        while i < len(prt):
            if(i-1>=len(rlt)):
                break
            flight.append(decimal.Decimal(prt[i]-rlt[i-1]))
            i+=1

        i = 0
        while i < len(prt)-3:
            if(i-1>= len(rlt)):
                break
            ngram.append(decimal.Decimal(rlt[i+3]-prt[i]))
            i+=1
        tt = []
        tt.append(decimal.Decimal(rlt[len(rlt)-1]-prt[0]))
        bla = []
        bla.append("sub00")
        master = master+bla+hold+flight+ngram+tt

        i = 0

        wb = xlsxwriter.Workbook("DataCollectedabc.xlsx")
        worksheet = wb.add_worksheet()
        # add_sheet is used to create sheet.

        i = 0
        while i < len(master):
            worksheet.write(0, i, master[i])
            i+=1
        wb.close()
        print ("done")
    else:
        print(len(prt),"\t",len(rlt))

if __name__ == "__main__":
    work = write2sheet()
