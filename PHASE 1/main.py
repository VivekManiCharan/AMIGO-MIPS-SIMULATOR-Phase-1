from tkinter import *
from decimal import *


class Main:

    def __init__(self):

        self.list1 = ["r0", "at", "v0", "v1", "a0", "a1", "a2", "a3", "t0", "t1",
                      "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "s0", "s1",
                      "s2", "s3", "s4", "s5", "s6", "s7", "s8", "k0", "k1", "gp", "sp", "ra"]
        self.list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def link_with_gui(self, gui):
        self.gui = gui

    def load(self, t):
        n = len(t)
        i = 0
        flag = 0
        flag2 = 0
        check = 0
        nxt = 0
        fi = t.find('li')
        if fi > -1 and fi + 8 <= n:
            nxt = fi + 2
            if fi > 0:
                while i < fi:
                    if t[i] == ' ' and t[i] != '\t':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ':
                check = 1
            if flag != 1 and check == 1:
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 4:
                            idx1 = 4 + temp1
                            flag2 = 1
                        elif temp == 115 and temp1 < 9:
                            idx1 = 18 + temp1
                            flag2 = 1
                        elif temp == 116 and temp1 < 10:
                            idx1 = 8 + temp1
                            flag2 = 1
                        elif temp == 118 and temp1 < 2:
                            idx1 = 2 + temp1
                            flag2 = 1
                        else:
                            flag2 = 0
                            self.print('in line' + str(count + 1) + 'error after ' + t[nxt])
                    else:
                        self.print('error after $')
                else:
                    self.print('no registers found')
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    start = nxt
                    while nxt < n:
                        if ord(t[nxt]) > 47 and ord(t[nxt]) < 58:
                            flag1 = 0
                        else:
                            flag1 = 1
                            self.print('in line ' + str(count + 1) + ' expected integer after ' + t[nxt - 1])
                            break
                        nxt = nxt + 1
                    if flag1 == 0 and flag2 == 1:
                        # self.print('command accepted at line ' + str(count+1))
                        newst = t[start:n]
                        val = Decimal(newst)
                        self.list2[idx1] = val
                        self.gui.tree.item(idx1, text="", values=(self.list1[idx1], val), tag  = 's')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after register')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('in line ' + str(count + 1) + ' instruction not found')

    def addi(self, t):
        n = len(t)
        i = 0
        flag = 0
        check1 = 0
        check2 = 0
        check3 = 0
        if t.find('addi') > -1 and t.find('addi') + 14 <= n:
            if t.find('addi') > 0:
                while i < t.find('addi'):
                    if t[i] != ' ':
                        flag = 1
                        break
                    i = i + 1
            if flag != 1:
                nxt = t.find('addi') + 4
                flag1 = 0
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            idx1 = 4 + temp1
                            check1 = 1
                        elif temp == 115 and temp1 < 9:
                            idx1 = 18 + temp1
                            check1 = 1
                        elif temp == 116 and temp1 < 9:
                            idx1 = 8 + temp1
                            check1 = 1
                        elif temp == 118 and temp1 < 3:
                            idx1 = 2 + temp1
                            check1 = 1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                    else:
                        self.print('in line' + str(count + 1) + ' error after 1st $')
                else:
                    self.print('in line ' + str(count + 1) + ' error after 1st comma')
                if t[nxt + 2] == ',':
                    nxt = nxt + 3
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(
                                t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check2 = 1
                                idx2 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check2 = 1
                                idx2 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check2 = 1
                                idx2 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check2 = 1
                                idx2 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 2nd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after addi')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after register')
                if t[nxt + 2] == ',':
                    nxt = nxt + 3
                    start = nxt
                    while nxt < n:
                        if ord(t[nxt]) > 47 and ord(t[nxt]) < 58:
                            nxt = nxt + 1
                        else:
                            self.print('in line ' + str(count + 1) + ' expected an "integer" after 2nd comma')
                            check3 = 1
                            break
                else:
                    self.print('in line ' + str(count + 1) + ' expected "," after 2nd register')
                if check1 == 1 and check2 == 1 and check3 == 0:
                    newst = t[start:n]
                    val = Decimal(newst)
                    self.list2[idx1] = self.list2[idx2] + val
                    self.gui.tree.item(idx1, text="", values=(self.list1[idx1], self.list2[idx1]), tag = 's')
                    # self.print('in line ' + str(count + 1) + ' command accepted')
            else:
                self.print('in line ' + str(count + 1) + ' error after addi')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    def store(self, t):
        n = len(t)
        i = 0
        flag = 0
        nxt = 0
        check = 0
        fi = t.find('st')
        if fi > -1 and fi + 8 <= n:
            nxt = fi + 2
            if fi > 0:
                while i < fi:
                    if t[i] != ' ' and t[i] != '\t':
                        flag = 1
                        break
                    i = i + 1
            if t[nxt] == ' ' or '\t':
                check = 1
            if flag != 1 and check == 1:
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            flag2 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            flag2 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            flag2 = 2
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            flag2 = 1
                            idx1 = 2 + temp1
                        else:
                            flag2 = 0
                        nxt = nxt + 2
                        if flag2 == 1:
                            if t[nxt] == ',':
                                nxt = nxt + 1
                                while t[nxt] == ' ':
                                    nxt = nxt + 1
                                start = nxt
                                while nxt < n:
                                    if ord(t[nxt]) > 47 and ord(t[nxt]) < 58:
                                        flag1 = 0
                                    else:
                                        flag1 = 1
                                        self.print(
                                            'in line ' + str(count + 1) + ' expected integer after ' + t[nxt - 1])
                                        break
                                    nxt = nxt + 1
                                if flag1 == 0:
                                    newst = t[start:n]
                                    val = Decimal(newst)
                                    self.list2[idx1] = val
                                    self.gui.tree.item(idx1, text="", values=(self.list1[idx1], val), tag = 's')
                                    #self.print('in line ' + str(count + 1) + ' command accepted at line ' + str(count))
                            else:
                                self.print('in line ' + str(count + 1) + ' expected , after register declaration')
                        else:
                            self.print('in line ' + str(count) + ' error in declaring registers')
                    else:
                        self.print('in line ' + ' error after 1st $')
                else:
                    self.print('expected $ after st')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('in line ' + str(count + 1) + ' command cannot be accepted')

    def sub(self, t):
        check1 = 0
        check2 = 0
        check3 = 0
        n = len(t)
        i = 0
        flag = 0
        check = 0
        fi = t.find('sub')
        if fi > -1 and fi + 15 <= n:
            if fi > 0:
                while i < fi:
                    if t[i] != ' ' and t[i] != '\t':
                        flag = 1
                        break
                    i = i + 1
            nxt = fi + 3
            if t[nxt] == ' ' or t[nxt] == '\t':
                check = 1
            nxt = nxt + 1
            if flag != 1 and check == 1:
                flag1 = 0
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st $')
                else:
                    self.print('in line ' + str(count + 1) + ' error after command')
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check2 = 1
                                idx2 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check2 = 1
                                idx2 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check2 = 1
                                idx2 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check2 = 1
                                idx2 = 2 + temp1
                            else:
                                self.print('n line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 2nd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st comma')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check3 = 1
                                idx3 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check3 = 1
                                idx3 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check3 = 1
                                idx3 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check3 = 1
                                idx3 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 3rd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd comma')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
                if check1 == 1 and check2 == 1 and check3 == 1:
                    self.list2[idx1] = self.list2[idx2] - self.list2[idx3]
                    self.gui.tree.item(idx1, text="", values=(self.list1[idx1], self.list2[idx1]), tag = 's')
                    # self.print('line ' + str(count + 1) + ' command accepted')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('in line ' + str(count + 1) + ' error at line-')

    def add(self, t):
        n = len(t)
        i = 0
        flag = 0
        check1 = 0
        check2 = 0
        check3 = 0
        check = 0
        fi = t.find('add')
        if fi > -1 and fi + 15 <= n:
            if fi > 0:
                while i < t.find('add'):
                    if t[i] != ' ' and t[i] != '\t':
                        flag = 1
                        break
                    i = i + 1
            nxt = fi + 3
            if t[nxt] == ' ' or t[nxt] == '\t':
                check = 1
            if flag != 1 and check == 1:
                flag1 = 0
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st $')
                else:
                    self.print('in line' + str(count + 1) + ' error after command')
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check2 = 1
                                idx2 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check2 = 1
                                idx2 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check2 = 1
                                idx2 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check2 = 1
                                idx2 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 2nd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st comma')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check3 = 1
                                idx3 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check3 = 1
                                idx3 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check3 = 1
                                idx3 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check3 = 1
                                idx3 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 3rd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd comma')
                    if check1 == 1 and check2 == 1 and check3 == 1:
                        self.list2[idx1] = self.list2[idx2] + self.list2[idx3]
                        self.gui.tree.item(idx1, text="", values=(self.list1[idx1], self.list2[idx1]), tag = 's')
                        # self.print('line ' + str(count + 1) + ' command accepted')
                else:
                    self.print(' in line ' + str(count) + 'expected , after ' + t[nxt - 1])
            else:
                self.print('in line ' + str(count + 1) + 'command not found')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    def jump(self, t, k):
        n = len(t)
        i = 0
        flag = 0
        flag2 = 0
        flag3 = 0
        nxt = 0
        fi = t.find('j')
        if fi > -1 and fi + 3 <= n:
            nxt = fi + 1
            if fi > 0:
                while i < fi:
                    if t[i] == ' ':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ' or t[nxt] == '\t':
                flag3 = 1
            nxt = nxt + 1
            if flag != 1 and flag3 == 1:
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                new = t[nxt:n]
                i = 0
                while i < len(k):
                    if k[i].find(new) > -1:
                        fin = k[i].find(new) + len(new)
                        if len(k[i]) > fin:
                            if k[i][fin] == ':':
                                flag2 = 1
                                break
                    i = i + 1
                if flag2 == 1:
                    # self.print('line ' + str(count + 1) + ' command accepted and jumped to instruction ' + str(i + 1))
                    return i - 1
                else:
                    self.print('in line ' + str(count + 1) + 'label of command not found')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('sorry')

    def bne(self, t, k):
        n = len(t)
        i = 0
        flag = 0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        check1 = 0
        check2 = 0
        check3 = 0
        nxt = 0
        n1 = len(k)
        fi = t.find('bne')
        if fi > -1 and fi + 13 <= n:
            nxt = fi + 3
            if fi > 0:
                while i < fi:
                    if t[i] == ' ' or t[i] == '\t':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ' or t[nxt] == '\t':
                flag3 = 1
            nxt = nxt + 1
            if flag != 1 and flag3 == 1:
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.gui.output.insert("insert", '\nin line ' + 'error after ' + t[nxt - 1])
                    else:
                        self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' error after $')
                else:
                    self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' expected $ after command')
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check2 = 1
                            idx2 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check2 = 1
                            idx2 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check2 = 1
                            idx2 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check2 = 1
                            idx2 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd $')
                else:
                    self.print('line ' + str(count + 1) + ' error after 1st comma')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                new = t[nxt:n]
                i = 0
                while i < n1:
                    if k[i].find(new) > -1:
                        fin = k[i].find(new) + len(new)
                        if len(k[i]) > fin:
                            if k[i][fin] == ':' and check1 == 1 and check2 == 1:
                                flag2 = 1
                                break
                    i = i + 1
                if flag2 == 1:
                    # self.print('in line ' + str(count + 1) + ' command accepted and jumped to instruction ' + str(i + 1))
                    if self.list2[idx1] != self.list2[idx2]:
                        return i - 1
                else:
                    self.print('in line ' + str(count + 1) + ' label of command not found')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after 2nd register')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    def slt(self, t, k):
        n = len(t)
        i = 0
        flag = 0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        check1 = 0
        check2 = 0
        check3 = 0
        nxt = 0
        n1 = len(k)
        fi = t.find('slt')
        if fi > -1 and fi + 13 <= n:
            nxt = fi + 3
            if fi > 0:
                while i < fi:
                    if t[i] == ' ' or t[i] == '\t':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ' or t[nxt] == '\t':
                flag3 = 1
            nxt = nxt + 1
            if flag != 1 and flag3 == 1:
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.gui.output.insert("insert", '\nin line ' + 'error after ' + t[nxt - 1])
                    else:
                        self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' error after $')
                else:
                    self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' expected $ after command')
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check2 = 1
                            idx2 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check2 = 1
                            idx2 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check2 = 1
                            idx2 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check2 = 1
                            idx2 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd $')
                else:
                    self.print('line ' + str(count + 1) + ' error after 1st comma')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                new = t[nxt:n]
                i = 0
                while i < n1:
                    if k[i].find(new) > -1:
                        fin = k[i].find(new) + len(new)
                        if len(k[i]) > fin:
                            if k[i][fin] == ':' and check1 == 1 and check2 == 1:
                                flag2 = 1
                                break
                    i = i + 1
                if flag2 == 1:
                    # self.print('in line ' + str(count + 1) + ' command accepted and jumped to instruction ' + str(i + 1))
                    if self.list2[idx1] < self.list2[idx2]:
                        return i - 1
                    else:
                        return count
                else:
                    self.print('in line ' + str(count + 1) + ' label of command not found')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after 2nd register')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    global count
    count = 0

    def print(self, str):
        self.gui.output.insert("insert", '\n' + str)

    def run(self):

        self.gui.save()

        self.gui.load()

        for i in range(0, 32):
            self.list2[i] = 0

        linstr = self.gui.text.get("1.0", END).splitlines()

        gth = len(linstr)
        global count
        count = 0

        self.print("--------------Running--------------------\n")

        while count < gth:
            if linstr[count].find('li') > -1:
                self.load(linstr[count])
            elif linstr[count].find('sub') > -1:
                self.sub(linstr[count])
            elif linstr[count].find('addi') > -1:
                self.addi(linstr[count])
            elif linstr[count].find('add') > -1:
                self.add(linstr[count])
            elif linstr[count].find('j') > -1:
                count = self.jump(linstr[count], linstr)
            elif linstr[count].find('bne') > -1:
                count = self.bne(linstr[count], linstr)
            elif linstr[count].find('slt') > -1:
                count = self.slt(linstr[count], linstr)
            elif linstr[count] == '':
                pass
            elif linstr[count][len(linstr[count]) - 1] == ':':
                pass
                # self.gui.output.insert("insert", '\nline ' + str(count + 1) + ' command accepted')
            elif linstr[count].find('.') > -1:
                ctr = 0
                while ctr < linstr[count].find('.'):
                    if linstr[count][ctr] == ' ' or linstr[count][ctr] == '\t':
                        pass
                    else:
                        self.gui.output.insert('insert', 'in line ' + str(count + 1) + ' instruction not found ')
                        break
                    ctr = ctr + 1
            elif linstr[count].find('#') > -1:
                ctr = 0
                while ctr < linstr[count].find('#'):
                    if linstr[count][ctr] == ' ' or linstr[count][ctr] == '\t':
                        pass
                    else:
                        self.gui.output.insert('insert', 'in line ' + str(count + 1) + ' instrucion not found')
                        break
                    ctr = ctr + 1
            elif linstr[count].find('st') > -1:
                self.store(linstr[count])
            else:
                self.gui.output.insert("insert", '\ninstruction not found at line ' + str(count + 1))
            count = count + 1

            self.print("\n--------------Terminated----------------\n")

