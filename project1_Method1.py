def print_Gandhi_ji():
    height = 101
    width = 100

    for row in range(height):
        for column in range(width):
            char = ' '

            if row == 0:
                if column == 0:
                    char = '*'
                elif column == 1:
                    char = '%'
                elif 2 <= column < 66:
                    char = '@'
                elif 66 <= column < 81:
                    char = '%'
                elif 81 <= column < 97:
                    char = '#'
                elif 97 <= column < 114:
                    char = '*'
                elif column == 114:
                    char = '+'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 118:
                    char = '+'
                elif column == 118:
                    char = '*'
                elif column == 119:
                    char = '%'

            elif row == 1:
                if 0 <= column < 2:
                    char = '+'
                elif column == 2:
                    char = '#'
                elif column == 3:
                    char = '%'
                elif 4 <= column < 71:
                    char = '@'
                elif 71 <= column < 85:
                    char = '%'
                elif 85 <= column < 101:
                    char = '#'
                elif 101 <= column < 117:
                    char = '*'
                elif column == 117:
                    char = '#'
                elif 118 <= column < 120:
                    char = '@'

            elif row == 2:
                if column == 0:
                    char = '*'
                elif 1 <= column < 3:
                    char = '+'
                elif 3 <= column < 73:
                    char = '*'
                elif 73 <= column < 102:
                    char = '+'
                elif column == 102:
                    char = '='
                elif column == 103:
                    char = '+'
                elif 104 <= column < 115:
                    char = '='
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 3:
                if column == 0:
                    char = '+'
                elif 1 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 9 <= column < 15:
                    char = '.'
                elif 31 <= column < 115:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 4:
                if column == 0:
                    char = '+'
                elif 1 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif 6 <= column < 8:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 5:
                if column == 0:
                    char = '+'
                elif 1 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif 6 <= column < 8:
                    char = '.'
                elif 10 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 6:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 7:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 15:
                    char = '*'
                elif column == 15:
                    char = '#'
                elif 16 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 8:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 9:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 10:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 11:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 12:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 13:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 14:
                if 0 <= column < 4:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '*'
                elif column == 12:
                    char = '#'
                elif 13 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 15:
                if 0 <= column < 5:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 51:
                    char = '*'
                elif 51 <= column < 57:
                    char = '+'
                elif column == 57:
                    char = '*'
                elif 58 <= column < 62:
                    char = '+'
                elif 62 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 16:
                if 0 <= column < 5:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 44:
                    char = '*'
                elif 44 <= column < 63:
                    char = '+'
                elif 63 <= column < 68:
                    char = '='
                elif 68 <= column < 71:
                    char = '+'
                elif 71 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 17:
                if 0 <= column < 3:
                    char = '*'
                elif column == 3:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 39:
                    char = '*'
                elif 39 <= column < 64:
                    char = '+'
                elif 64 <= column < 74:
                    char = '='
                elif column == 74:
                    char = '+'
                elif 75 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 18:
                if column == 0:
                    char = '*'
                elif 1 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 37:
                    char = '*'
                elif 37 <= column < 52:
                    char = '+'
                elif 52 <= column < 74:
                    char = '='
                elif 74 <= column < 77:
                    char = '-'
                elif column == 77:
                    char = '='
                elif column == 78:
                    char = '+'
                elif 79 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 19:
                if column == 0:
                    char = '*'
                elif 1 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 39:
                    char = '*'
                elif 39 <= column < 50:
                    char = '+'
                elif 50 <= column < 76:
                    char = '='
                elif 76 <= column < 80:
                    char = '-'
                elif column == 80:
                    char = '='
                elif column == 81:
                    char = '+'
                elif 82 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 20:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 31:
                    char = '*'
                elif 31 <= column < 34:
                    char = '+'
                elif 34 <= column < 39:
                    char = '*'
                elif 39 <= column < 48:
                    char = '+'
                elif 48 <= column < 66:
                    char = '='
                elif 66 <= column < 73:
                    char = '-'
                elif column == 73:
                    char = '='
                elif 74 <= column < 76:
                    char = '-'
                elif column == 76:
                    char = '='
                elif 77 <= column < 81:
                    char = '-'
                elif column == 81:
                    char = ':'
                elif column == 82:
                    char = '-'
                elif column == 83:
                    char = '+'
                elif 84 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 21:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 29:
                    char = '*'
                elif 29 <= column < 34:
                    char = '+'
                elif 34 <= column < 38:
                    char = '*'
                elif 38 <= column < 46:
                    char = '+'
                elif 46 <= column < 62:
                    char = '='
                elif 62 <= column < 83:
                    char = '-'
                elif column == 83:
                    char = ':'
                elif column == 84:
                    char = '-'
                elif column == 85:
                    char = '+'
                elif 86 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 22:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 28:
                    char = '*'
                elif column == 28:
                    char = '+'
                elif column == 29:
                    char = '='
                elif 30 <= column < 34:
                    char = '+'
                elif 34 <= column < 37:
                    char = '*'
                elif 37 <= column < 45:
                    char = '+'
                elif 45 <= column < 60:
                    char = '='
                elif 60 <= column < 84:
                    char = '-'
                elif 84 <= column < 86:
                    char = ':'
                elif column == 86:
                    char = '-'
                elif 87 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 23:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 27:
                    char = '*'
                elif column == 27:
                    char = '+'
                elif column == 28:
                    char = '='
                elif 29 <= column < 31:
                    char = '-'
                elif 31 <= column < 33:
                    char = '='
                elif column == 33:
                    char = '+'
                elif 34 <= column < 37:
                    char = '*'
                elif 37 <= column < 45:
                    char = '+'
                elif 45 <= column < 59:
                    char = '='
                elif 59 <= column < 86:
                    char = '-'
                elif 86 <= column < 88:
                    char = ':'
                elif column == 88:
                    char = '+'
                elif 89 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 24:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 27:
                    char = '*'
                elif column == 27:
                    char = '+'
                elif 28 <= column < 31:
                    char = '-'
                elif 31 <= column < 33:
                    char = '='
                elif column == 33:
                    char = '+'
                elif 34 <= column < 36:
                    char = '*'
                elif 36 <= column < 44:
                    char = '+'
                elif 44 <= column < 58:
                    char = '='
                elif 58 <= column < 70:
                    char = '-'
                elif 70 <= column < 77:
                    char = ':'
                elif 77 <= column < 88:
                    char = '-'
                elif column == 88:
                    char = ':'
                elif column == 89:
                    char = '-'
                elif 90 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 25:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 26:
                    char = '*'
                elif column == 26:
                    char = '+'
                elif column == 27:
                    char = '='
                elif 28 <= column < 32:
                    char = '-'
                elif column == 32:
                    char = '='
                elif column == 33:
                    char = '+'
                elif 34 <= column < 36:
                    char = '*'
                elif 36 <= column < 43:
                    char = '+'
                elif 43 <= column < 57:
                    char = '='
                elif 57 <= column < 68:
                    char = '-'
                elif 68 <= column < 78:
                    char = ':'
                elif 78 <= column < 89:
                    char = '-'
                elif 89 <= column < 91:
                    char = ':'
                elif column == 91:
                    char = '+'
                elif 92 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 26:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 25:
                    char = '*'
                elif column == 25:
                    char = '+'
                elif column == 26:
                    char = '='
                elif 27 <= column < 32:
                    char = '-'
                elif column == 32:
                    char = '='
                elif column == 33:
                    char = '+'
                elif 34 <= column < 36:
                    char = '*'
                elif 36 <= column < 42:
                    char = '+'
                elif 42 <= column < 57:
                    char = '='
                elif 57 <= column < 69:
                    char = '-'
                elif 69 <= column < 78:
                    char = ':'
                elif 78 <= column < 90:
                    char = '-'
                elif 90 <= column < 92:
                    char = ':'
                elif column == 92:
                    char = '='
                elif 93 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 27:
                if 0 <= column < 4:
                    char = '#'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 24:
                    char = '*'
                elif column == 24:
                    char = '+'
                elif 25 <= column < 27:
                    char = '='
                elif 27 <= column < 33:
                    char = '-'
                elif column == 33:
                    char = '='
                elif column == 34:
                    char = '+'
                elif column == 35:
                    char = '*'
                elif 36 <= column < 41:
                    char = '+'
                elif 41 <= column < 59:
                    char = '='
                elif 59 <= column < 72:
                    char = '-'
                elif 72 <= column < 74:
                    char = ':'
                elif 74 <= column < 92:
                    char = '-'
                elif column == 92:
                    char = ':'
                elif column == 93:
                    char = '-'
                elif 94 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 28:
                if 0 <= column < 3:
                    char = '#'
                elif column == 3:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 24:
                    char = '*'
                elif column == 24:
                    char = '+'
                elif 25 <= column < 29:
                    char = '='
                elif 29 <= column < 33:
                    char = '-'
                elif column == 33:
                    char = '='
                elif 34 <= column < 41:
                    char = '+'
                elif 41 <= column < 59:
                    char = '='
                elif 59 <= column < 90:
                    char = '-'
                elif column == 90:
                    char = '='
                elif 91 <= column < 93:
                    char = '-'
                elif column == 93:
                    char = ':'
                elif column == 94:
                    char = '='
                elif 95 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 29:
                if 0 <= column < 3:
                    char = '#'
                elif column == 3:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 24:
                    char = '*'
                elif column == 24:
                    char = '+'
                elif 25 <= column < 28:
                    char = '='
                elif 28 <= column < 34:
                    char = '-'
                elif column == 34:
                    char = '+'
                elif column == 35:
                    char = '*'
                elif 36 <= column < 42:
                    char = '+'
                elif 42 <= column < 60:
                    char = '='
                elif 60 <= column < 71:
                    char = '-'
                elif column == 71:
                    char = ':'
                elif column == 72:
                    char = '-'
                elif 73 <= column < 76:
                    char = ':'
                elif 76 <= column < 93:
                    char = '-'
                elif 93 <= column < 95:
                    char = ':'
                elif column == 95:
                    char = '='
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 30:
                if column == 0:
                    char = '#'
                elif column == 1:
                    char = '%'
                elif column == 2:
                    char = '#'
                elif column == 3:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 24:
                    char = '*'
                elif column == 24:
                    char = '+'
                elif 25 <= column < 27:
                    char = '='
                elif column == 27:
                    char = '-'
                elif 28 <= column < 30:
                    char = ':'
                elif 30 <= column < 33:
                    char = '-'
                elif 33 <= column < 35:
                    char = '='
                elif 35 <= column < 42:
                    char = '+'
                elif 42 <= column < 61:
                    char = '='
                elif column == 61:
                    char = '-'
                elif 62 <= column < 68:
                    char = '='
                elif 68 <= column < 88:
                    char = '-'
                elif column == 88:
                    char = '='
                elif 89 <= column < 94:
                    char = '-'
                elif 94 <= column < 96:
                    char = ':'
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 31:
                if column == 0:
                    char = '#'
                elif 1 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 23:
                    char = '*'
                elif column == 23:
                    char = '+'
                elif 24 <= column < 27:
                    char = '='
                elif 27 <= column < 34:
                    char = '-'
                elif column == 34:
                    char = '='
                elif 35 <= column < 44:
                    char = '+'
                elif 44 <= column < 66:
                    char = '='
                elif 66 <= column < 94:
                    char = '-'
                elif 94 <= column < 96:
                    char = ':'
                elif column == 96:
                    char = '='
                elif 97 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 32:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 23:
                    char = '*'
                elif column == 23:
                    char = '+'
                elif 24 <= column < 26:
                    char = '='
                elif column == 26:
                    char = '-'
                elif 27 <= column < 29:
                    char = '='
                elif 29 <= column < 34:
                    char = '-'
                elif column == 34:
                    char = '='
                elif 35 <= column < 40:
                    char = '+'
                elif 40 <= column < 42:
                    char = '='
                elif 42 <= column < 45:
                    char = '+'
                elif 45 <= column < 49:
                    char = '='
                elif column == 49:
                    char = '-'
                elif 50 <= column < 59:
                    char = '='
                elif column == 59:
                    char = '+'
                elif 60 <= column < 71:
                    char = '='
                elif column == 71:
                    char = '-'
                elif column == 72:
                    char = '='
                elif 73 <= column < 79:
                    char = '-'
                elif 79 <= column < 81:
                    char = '='
                elif 81 <= column < 95:
                    char = '-'
                elif column == 95:
                    char = ':'
                elif column == 96:
                    char = '-'
                elif 97 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 33:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 23:
                    char = '*'
                elif 23 <= column < 25:
                    char = '+'
                elif column == 25:
                    char = '='
                elif 26 <= column < 33:
                    char = '-'
                elif 33 <= column < 36:
                    char = '='
                elif 36 <= column < 42:
                    char = '+'
                elif 42 <= column < 59:
                    char = '='
                elif 59 <= column < 61:
                    char = '+'
                elif 61 <= column < 67:
                    char = '='
                elif 67 <= column < 74:
                    char = '-'
                elif 74 <= column < 79:
                    char = '='
                elif 79 <= column < 95:
                    char = '-'
                elif 95 <= column < 97:
                    char = ':'
                elif 97 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 34:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 20:
                    char = '*'
                elif 20 <= column < 24:
                    char = '+'
                elif 24 <= column < 26:
                    char = '='
                elif column == 26:
                    char = '-'
                elif column == 27:
                    char = '='
                elif 28 <= column < 30:
                    char = '-'
                elif column == 30:
                    char = ':'
                elif 31 <= column < 34:
                    char = '-'
                elif column == 34:
                    char = '='
                elif 35 <= column < 42:
                    char = '+'
                elif 42 <= column < 64:
                    char = '='
                elif 64 <= column < 71:
                    char = '-'
                elif 71 <= column < 74:
                    char = ':'
                elif 74 <= column < 78:
                    char = '-'
                elif 78 <= column < 80:
                    char = '='
                elif 80 <= column < 82:
                    char = '-'
                elif 82 <= column < 86:
                    char = ':'
                elif 86 <= column < 95:
                    char = '-'
                elif 95 <= column < 97:
                    char = ':'
                elif 97 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 35:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '*'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 17:
                    char = '*'
                elif 17 <= column < 19:
                    char = '+'
                elif 19 <= column < 23:
                    char = '='
                elif 23 <= column < 25:
                    char = '-'
                elif column == 25:
                    char = ':'
                elif column == 26:
                    char = '='
                elif 27 <= column < 29:
                    char = '#'
                elif column == 29:
                    char = '*'
                elif column == 30:
                    char = '+'
                elif column == 31:
                    char = '='
                elif column == 32:
                    char = '-'
                elif column == 33:
                    char = '='
                elif 34 <= column < 43:
                    char = '+'
                elif 43 <= column < 60:
                    char = '='
                elif 60 <= column < 71:
                    char = '-'
                elif 71 <= column < 79:
                    char = ':'
                elif 79 <= column < 94:
                    char = '-'
                elif 94 <= column < 97:
                    char = ':'
                elif column == 97:
                    char = '+'
                elif 98 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 36:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 16:
                    char = '*'
                elif column == 16:
                    char = '+'
                elif column == 17:
                    char = '='
                elif column == 18:
                    char = '+'
                elif 19 <= column < 21:
                    char = '*'
                elif 21 <= column < 24:
                    char = '#'
                elif column == 24:
                    char = '*'
                elif column == 25:
                    char = '='
                elif column == 26:
                    char = ':'
                elif column == 27:
                    char = '-'
                elif column == 28:
                    char = '+'
                elif column == 29:
                    char = '*'
                elif column == 30:
                    char = '#'
                elif column == 31:
                    char = '%'
                elif 32 <= column < 34:
                    char = '#'
                elif 34 <= column < 36:
                    char = '*'
                elif 36 <= column < 44:
                    char = '+'
                elif 44 <= column < 59:
                    char = '='
                elif 59 <= column < 76:
                    char = '-'
                elif 76 <= column < 81:
                    char = ':'
                elif 81 <= column < 87:
                    char = '-'
                elif 87 <= column < 93:
                    char = ':'
                elif column == 93:
                    char = '-'
                elif 94 <= column < 97:
                    char = ':'
                elif column == 97:
                    char = '+'
                elif 98 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 37:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 15:
                    char = '*'
                elif 15 <= column < 17:
                    char = '+'
                elif column == 17:
                    char = '*'
                elif column == 18:
                    char = '#'
                elif column == 19:
                    char = '*'
                elif 20 <= column < 23:
                    char = '+'
                elif 23 <= column < 26:
                    char = '#'
                elif column == 26:
                    char = '*'
                elif column == 27:
                    char = '='
                elif 28 <= column < 30:
                    char = '-'
                elif column == 30:
                    char = '='
                elif column == 31:
                    char = '+'
                elif column == 32:
                    char = '*'
                elif column == 33:
                    char = '#'
                elif 34 <= column < 36:
                    char = '%'
                elif 36 <= column < 38:
                    char = '#'
                elif column == 38:
                    char = '*'
                elif 39 <= column < 45:
                    char = '+'
                elif 45 <= column < 48:
                    char = '='
                elif column == 48:
                    char = '-'
                elif 49 <= column < 60:
                    char = '='
                elif 60 <= column < 64:
                    char = '-'
                elif 64 <= column < 67:
                    char = '='
                elif 67 <= column < 71:
                    char = '+'
                elif 71 <= column < 76:
                    char = '*'
                elif column == 76:
                    char = '+'
                elif column == 77:
                    char = '='
                elif 78 <= column < 88:
                    char = '-'
                elif 88 <= column < 92:
                    char = ':'
                elif 92 <= column < 94:
                    char = '-'
                elif 94 <= column < 98:
                    char = ':'
                elif 98 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 38:
                if 0 <= column < 4:
                    char = '%'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 14:
                    char = '*'
                elif 14 <= column < 16:
                    char = '+'
                elif 16 <= column < 19:
                    char = '*'
                elif column == 19:
                    char = '+'
                elif column == 20:
                    char = '-'
                elif column == 21:
                    char = '='
                elif column == 22:
                    char = '+'
                elif 23 <= column < 27:
                    char = '*'
                elif 27 <= column < 30:
                    char = '+'
                elif 30 <= column < 33:
                    char = '='
                elif column == 33:
                    char = '+'
                elif 34 <= column < 36:
                    char = '*'
                elif 36 <= column < 41:
                    char = '#'
                elif column == 41:
                    char = '*'
                elif column == 42:
                    char = '+'
                elif 43 <= column < 50:
                    char = '='
                elif 50 <= column < 53:
                    char = '-'
                elif 53 <= column < 61:
                    char = '='
                elif column == 61:
                    char = '+'
                elif 62 <= column < 64:
                    char = '*'
                elif 64 <= column < 68:
                    char = '#'
                elif 68 <= column < 74:
                    char = '%'
                elif 74 <= column < 79:
                    char = '#'
                elif column == 79:
                    char = '*'
                elif 80 <= column < 82:
                    char = '='
                elif 82 <= column < 84:
                    char = '-'
                elif 84 <= column < 86:
                    char = '='
                elif 86 <= column < 92:
                    char = '-'
                elif 92 <= column < 95:
                    char = '='
                elif 95 <= column < 97:
                    char = '-'
                elif column == 97:
                    char = '.'
                elif column == 98:
                    char = '+'
                elif 99 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 39:
                if 0 <= column < 3:
                    char = '%'
                elif column == 3:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 14:
                    char = '*'
                elif 14 <= column < 16:
                    char = '+'
                elif column == 16:
                    char = '*'
                elif 17 <= column < 20:
                    char = '+'
                elif 20 <= column < 22:
                    char = '-'
                elif column == 22:
                    char = '='
                elif column == 23:
                    char = '+'
                elif 24 <= column < 26:
                    char = '='
                elif 26 <= column < 32:
                    char = '+'
                elif 32 <= column < 34:
                    char = '='
                elif column == 34:
                    char = '+'
                elif 35 <= column < 37:
                    char = '*'
                elif 37 <= column < 40:
                    char = '+'
                elif column == 40:
                    char = '*'
                elif 41 <= column < 44:
                    char = '#'
                elif column == 44:
                    char = '*'
                elif column == 45:
                    char = '+'
                elif 46 <= column < 56:
                    char = '='
                elif column == 56:
                    char = '-'
                elif 57 <= column < 60:
                    char = '='
                elif column == 60:
                    char = '+'
                elif 61 <= column < 64:
                    char = '*'
                elif 64 <= column < 69:
                    char = '+'
                elif 69 <= column < 71:
                    char = '*'
                elif 71 <= column < 79:
                    char = '+'
                elif 79 <= column < 81:
                    char = '%'
                elif column == 81:
                    char = '*'
                elif 82 <= column < 84:
                    char = '+'
                elif 84 <= column < 86:
                    char = '='
                elif 86 <= column < 88:
                    char = '-'
                elif column == 88:
                    char = '='
                elif 89 <= column < 91:
                    char = '*'
                elif 91 <= column < 94:
                    char = '#'
                elif 94 <= column < 96:
                    char = '*'
                elif column == 96:
                    char = '='
                elif column == 97:
                    char = ':'
                elif 98 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 40:
                if 0 <= column < 3:
                    char = '%'
                elif column == 3:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 14:
                    char = '*'
                elif 14 <= column < 16:
                    char = '+'
                elif column == 16:
                    char = '*'
                elif 17 <= column < 20:
                    char = '+'
                elif 20 <= column < 22:
                    char = '-'
                elif 22 <= column < 26:
                    char = '='
                elif 26 <= column < 30:
                    char = '*'
                elif column == 30:
                    char = '+'
                elif 31 <= column < 34:
                    char = '='
                elif column == 34:
                    char = '+'
                elif 35 <= column < 37:
                    char = '*'
                elif 37 <= column < 40:
                    char = '+'
                elif column == 40:
                    char = '='
                elif column == 41:
                    char = '-'
                elif 42 <= column < 44:
                    char = '='
                elif column == 44:
                    char = '+'
                elif column == 45:
                    char = '*'
                elif column == 46:
                    char = '#'
                elif column == 47:
                    char = '+'
                elif 48 <= column < 56:
                    char = '='
                elif 56 <= column < 60:
                    char = '+'
                elif column == 60:
                    char = '*'
                elif column == 61:
                    char = '+'
                elif 62 <= column < 64:
                    char = '='
                elif 64 <= column < 67:
                    char = '+'
                elif 67 <= column < 69:
                    char = '*'
                elif column == 69:
                    char = '+'
                elif column == 70:
                    char = '='
                elif column == 71:
                    char = '+'
                elif 72 <= column < 77:
                    char = '*'
                elif column == 77:
                    char = '#'
                elif column == 78:
                    char = '*'
                elif column == 79:
                    char = '='
                elif 80 <= column < 82:
                    char = '%'
                elif column == 82:
                    char = '#'
                elif column == 83:
                    char = '+'
                elif 84 <= column < 86:
                    char = '='
                elif column == 86:
                    char = '-'
                elif column == 87:
                    char = '='
                elif column == 88:
                    char = '#'
                elif column == 89:
                    char = '%'
                elif column == 90:
                    char = '*'
                elif 91 <= column < 93:
                    char = '+'
                elif 93 <= column < 99:
                    char = '='
                elif 99 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 41:
                if 0 <= column < 3:
                    char = '%'
                elif column == 3:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 14:
                    char = '*'
                elif 14 <= column < 16:
                    char = '+'
                elif column == 16:
                    char = '*'
                elif column == 17:
                    char = '+'
                elif column == 18:
                    char = '*'
                elif column == 19:
                    char = '+'
                elif column == 20:
                    char = '-'
                elif column == 21:
                    char = '+'
                elif 22 <= column < 27:
                    char = '*'
                elif 27 <= column < 30:
                    char = '#'
                elif column == 30:
                    char = '='
                elif column == 31:
                    char = '-'
                elif 32 <= column < 34:
                    char = '='
                elif column == 34:
                    char = '+'
                elif 35 <= column < 37:
                    char = '*'
                elif 37 <= column < 40:
                    char = '+'
                elif 40 <= column < 42:
                    char = '='
                elif 42 <= column < 47:
                    char = '-'
                elif column == 47:
                    char = '='
                elif 48 <= column < 53:
                    char = '+'
                elif 53 <= column < 57:
                    char = '='
                elif 57 <= column < 60:
                    char = '+'
                elif 60 <= column < 62:
                    char = '*'
                elif 62 <= column < 66:
                    char = '#'
                elif column == 66:
                    char = '+'
                elif 67 <= column < 69:
                    char = '*'
                elif column == 69:
                    char = '+'
                elif 70 <= column < 72:
                    char = '#'
                elif 72 <= column < 75:
                    char = '%'
                elif 75 <= column < 77:
                    char = '#'
                elif column == 77:
                    char = '*'
                elif column == 78:
                    char = '#'
                elif 79 <= column < 81:
                    char = '+'
                elif column == 81:
                    char = '#'
                elif column == 82:
                    char = '*'
                elif 83 <= column < 85:
                    char = '+'
                elif column == 85:
                    char = '='
                elif column == 86:
                    char = '+'
                elif 87 <= column < 89:
                    char = '#'
                elif column == 89:
                    char = '='
                elif column == 90:
                    char = '+'
                elif 91 <= column < 94:
                    char = '*'
                elif column == 94:
                    char = '='
                elif column == 95:
                    char = '-'
                elif column == 96:
                    char = ':'
                elif 97 <= column < 99:
                    char = '+'
                elif column == 99:
                    char = '='
                elif 100 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 42:
                if 0 <= column < 3:
                    char = '%'
                elif column == 3:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 15:
                    char = '*'
                elif 15 <= column < 17:
                    char = '+'
                elif 17 <= column < 19:
                    char = '*'
                elif 19 <= column < 21:
                    char = '='
                elif column == 21:
                    char = '*'
                elif 22 <= column < 24:
                    char = '#'
                elif 24 <= column < 27:
                    char = '*'
                elif 27 <= column < 29:
                    char = '#'
                elif column == 29:
                    char = '*'
                elif 30 <= column < 32:
                    char = '-'
                elif 32 <= column < 34:
                    char = '='
                elif column == 34:
                    char = '+'
                elif 35 <= column < 37:
                    char = '*'
                elif 37 <= column < 40:
                    char = '+'
                elif 40 <= column < 43:
                    char = '='
                elif 43 <= column < 48:
                    char = '-'
                elif 48 <= column < 51:
                    char = '='
                elif 51 <= column < 54:
                    char = '+'
                elif column == 54:
                    char = '*'
                elif 55 <= column < 57:
                    char = '+'
                elif 57 <= column < 59:
                    char = '='
                elif 59 <= column < 63:
                    char = '+'
                elif 63 <= column < 65:
                    char = '='
                elif 65 <= column < 68:
                    char = '+'
                elif column == 68:
                    char = '='
                elif 69 <= column < 71:
                    char = '*'
                elif column == 71:
                    char = '#'
                elif column == 72:
                    char = '*'
                elif column == 73:
                    char = '+'
                elif 74 <= column < 79:
                    char = '#'
                elif column == 79:
                    char = '+'
                elif column == 80:
                    char = '='
                elif column == 81:
                    char = '*'
                elif 82 <= column < 84:
                    char = '+'
                elif column == 84:
                    char = '='
                elif column == 85:
                    char = '-'
                elif 86 <= column < 88:
                    char = '#'
                elif column == 88:
                    char = '='
                elif column == 89:
                    char = '*'
                elif column == 90:
                    char = '%'
                elif 91 <= column < 93:
                    char = '#'
                elif column == 93:
                    char = '*'
                elif column == 94:
                    char = '#'
                elif column == 95:
                    char = '+'
                elif column == 96:
                    char = '-'
                elif 97 <= column < 99:
                    char = '*'
                elif column == 99:
                    char = '-'
                elif 100 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 43:
                if column == 0:
                    char = '%'
                elif column == 1:
                    char = '@'
                elif column == 2:
                    char = '%'
                elif column == 3:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 16:
                    char = '*'
                elif 16 <= column < 18:
                    char = '+'
                elif column == 18:
                    char = '*'
                elif column == 19:
                    char = '+'
                elif column == 20:
                    char = '='
                elif column == 21:
                    char = '+'
                elif column == 22:
                    char = '*'
                elif 23 <= column < 25:
                    char = '+'
                elif 25 <= column < 28:
                    char = '*'
                elif column == 28:
                    char = '#'
                elif column == 29:
                    char = '+'
                elif column == 30:
                    char = '-'
                elif 31 <= column < 33:
                    char = '='
                elif 33 <= column < 35:
                    char = '+'
                elif 35 <= column < 37:
                    char = '*'
                elif 37 <= column < 41:
                    char = '+'
                elif 41 <= column < 44:
                    char = '='
                elif 44 <= column < 47:
                    char = '-'
                elif 47 <= column < 59:
                    char = '='
                elif 59 <= column < 61:
                    char = '+'
                elif column == 61:
                    char = '='
                elif 62 <= column < 64:
                    char = '+'
                elif column == 64:
                    char = '*'
                elif 65 <= column < 67:
                    char = '+'
                elif column == 67:
                    char = '='
                elif 68 <= column < 71:
                    char = '+'
                elif 71 <= column < 75:
                    char = '*'
                elif 75 <= column < 77:
                    char = '#'
                elif column == 77:
                    char = '*'
                elif column == 78:
                    char = '+'
                elif column == 79:
                    char = '='
                elif column == 80:
                    char = '+'
                elif column == 81:
                    char = '*'
                elif column == 82:
                    char = '+'
                elif column == 83:
                    char = '='
                elif 84 <= column < 86:
                    char = '-'
                elif column == 86:
                    char = '*'
                elif column == 87:
                    char = '='
                elif column == 88:
                    char = '+'
                elif 89 <= column < 92:
                    char = '#'
                elif column == 92:
                    char = '+'
                elif column == 93:
                    char = '-'
                elif 94 <= column < 96:
                    char = '+'
                elif column == 96:
                    char = '='
                elif column == 97:
                    char = '+'
                elif column == 98:
                    char = '*'
                elif column == 99:
                    char = '='
                elif column == 100:
                    char = '+'
                elif 101 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 44:
                if column == 0:
                    char = '%'
                elif column == 1:
                    char = '@'
                elif column == 2:
                    char = '%'
                elif column == 3:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 17:
                    char = '*'
                elif 17 <= column < 19:
                    char = '+'
                elif column == 19:
                    char = '*'
                elif column == 20:
                    char = '+'
                elif column == 21:
                    char = '='
                elif column == 22:
                    char = '+'
                elif 23 <= column < 28:
                    char = '='
                elif column == 28:
                    char = '*'
                elif column == 29:
                    char = '#'
                elif 30 <= column < 33:
                    char = '+'
                elif 33 <= column < 38:
                    char = '*'
                elif 38 <= column < 41:
                    char = '+'
                elif 41 <= column < 54:
                    char = '='
                elif 54 <= column < 56:
                    char = '-'
                elif 56 <= column < 63:
                    char = '='
                elif column == 63:
                    char = '+'
                elif 64 <= column < 67:
                    char = '*'
                elif column == 67:
                    char = '+'
                elif 68 <= column < 73:
                    char = '*'
                elif 73 <= column < 76:
                    char = '+'
                elif 76 <= column < 78:
                    char = '='
                elif column == 78:
                    char = '+'
                elif 79 <= column < 83:
                    char = '='
                elif 83 <= column < 85:
                    char = '-'
                elif column == 85:
                    char = ':'
                elif column == 86:
                    char = '-'
                elif column == 87:
                    char = '+'
                elif column == 88:
                    char = '*'
                elif column == 89:
                    char = '+'
                elif 90 <= column < 93:
                    char = '='
                elif column == 93:
                    char = '-'
                elif column == 94:
                    char = ':'
                elif column == 95:
                    char = '-'
                elif 96 <= column < 99:
                    char = '+'
                elif 99 <= column < 101:
                    char = '='
                elif 101 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 45:
                if column == 0:
                    char = '%'
                elif 1 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 16:
                    char = '*'
                elif column == 16:
                    char = '+'
                elif column == 17:
                    char = '*'
                elif 18 <= column < 20:
                    char = '+'
                elif column == 20:
                    char = '*'
                elif column == 21:
                    char = '+'
                elif 22 <= column < 25:
                    char = '='
                elif 25 <= column < 27:
                    char = '-'
                elif column == 27:
                    char = '='
                elif column == 28:
                    char = '+'
                elif 29 <= column < 31:
                    char = '*'
                elif column == 31:
                    char = '+'
                elif column == 32:
                    char = '*'
                elif 33 <= column < 35:
                    char = '#'
                elif 35 <= column < 38:
                    char = '*'
                elif 38 <= column < 42:
                    char = '+'
                elif 42 <= column < 53:
                    char = '='
                elif 53 <= column < 64:
                    char = '-'
                elif column == 64:
                    char = '='
                elif column == 65:
                    char = '-'
                elif column == 66:
                    char = '+'
                elif 67 <= column < 69:
                    char = '='
                elif 69 <= column < 78:
                    char = '-'
                elif column == 78:
                    char = '+'
                elif column == 79:
                    char = '='
                elif column == 80:
                    char = '-'
                elif 81 <= column < 86:
                    char = ':'
                elif column == 86:
                    char = '.'
                elif column == 87:
                    char = '='
                elif 88 <= column < 90:
                    char = '*'
                elif 90 <= column < 92:
                    char = '+'
                elif column == 92:
                    char = '='
                elif column == 93:
                    char = '-'
                elif column == 94:
                    char = ':'
                elif column == 95:
                    char = '='
                elif 96 <= column < 98:
                    char = '*'
                elif column == 98:
                    char = '='
                elif column == 99:
                    char = '+'
                elif 100 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 46:
                if column == 0:
                    char = '%'
                elif 1 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 19:
                    char = '*'
                elif 19 <= column < 22:
                    char = '+'
                elif 22 <= column < 24:
                    char = '*'
                elif 24 <= column < 31:
                    char = '+'
                elif 31 <= column < 38:
                    char = '*'
                elif 38 <= column < 43:
                    char = '+'
                elif 43 <= column < 53:
                    char = '='
                elif 53 <= column < 62:
                    char = '-'
                elif 62 <= column < 64:
                    char = ':'
                elif column == 64:
                    char = '-'
                elif column == 65:
                    char = ':'
                elif column == 66:
                    char = '-'
                elif column == 67:
                    char = '='
                elif column == 68:
                    char = '-'
                elif 69 <= column < 72:
                    char = ':'
                elif 72 <= column < 75:
                    char = '-'
                elif 75 <= column < 79:
                    char = '='
                elif 79 <= column < 81:
                    char = '-'
                elif 81 <= column < 88:
                    char = ':'
                elif column == 88:
                    char = '-'
                elif column == 89:
                    char = '='
                elif 90 <= column < 92:
                    char = '-'
                elif 92 <= column < 95:
                    char = ':'
                elif column == 95:
                    char = '-'
                elif column == 96:
                    char = '*'
                elif column == 97:
                    char = '='
                elif column == 98:
                    char = '+'
                elif 99 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 47:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 20:
                    char = '*'
                elif 20 <= column < 22:
                    char = '+'
                elif 22 <= column < 24:
                    char = '='
                elif 24 <= column < 28:
                    char = '+'
                elif column == 28:
                    char = '*'
                elif column == 29:
                    char = '+'
                elif column == 30:
                    char = '='
                elif 31 <= column < 33:
                    char = '-'
                elif column == 33:
                    char = '='
                elif 34 <= column < 36:
                    char = '+'
                elif 36 <= column < 38:
                    char = '*'
                elif 38 <= column < 42:
                    char = '+'
                elif 42 <= column < 54:
                    char = '='
                elif 54 <= column < 61:
                    char = '-'
                elif 61 <= column < 67:
                    char = ':'
                elif 67 <= column < 69:
                    char = '='
                elif 69 <= column < 73:
                    char = '-'
                elif 73 <= column < 76:
                    char = '='
                elif column == 76:
                    char = '+'
                elif column == 77:
                    char = '='
                elif 78 <= column < 83:
                    char = '-'
                elif 83 <= column < 89:
                    char = ':'
                elif 89 <= column < 92:
                    char = '-'
                elif 92 <= column < 95:
                    char = ':'
                elif column == 95:
                    char = '-'
                elif column == 96:
                    char = '+'
                elif 97 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 48:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 21:
                    char = '*'
                elif 21 <= column < 24:
                    char = '+'
                elif 24 <= column < 26:
                    char = '='
                elif 26 <= column < 33:
                    char = '-'
                elif column == 33:
                    char = '='
                elif 34 <= column < 36:
                    char = '+'
                elif 36 <= column < 38:
                    char = '*'
                elif 38 <= column < 42:
                    char = '+'
                elif 42 <= column < 55:
                    char = '='
                elif 55 <= column < 66:
                    char = '-'
                elif 66 <= column < 68:
                    char = '='
                elif 68 <= column < 73:
                    char = '+'
                elif 73 <= column < 75:
                    char = '*'
                elif 75 <= column < 77:
                    char = '+'
                elif 77 <= column < 81:
                    char = '='
                elif 81 <= column < 84:
                    char = '-'
                elif 84 <= column < 90:
                    char = ':'
                elif column == 90:
                    char = '='
                elif 91 <= column < 94:
                    char = '-'
                elif column == 94:
                    char = '='
                elif column == 95:
                    char = '-'
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 49:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 22:
                    char = '*'
                elif 22 <= column < 27:
                    char = '+'
                elif 27 <= column < 33:
                    char = '='
                elif 33 <= column < 38:
                    char = '*'
                elif 38 <= column < 43:
                    char = '+'
                elif 43 <= column < 64:
                    char = '='
                elif 64 <= column < 69:
                    char = '+'
                elif 69 <= column < 71:
                    char = '*'
                elif 71 <= column < 73:
                    char = '#'
                elif column == 73:
                    char = '*'
                elif column == 74:
                    char = '='
                elif 75 <= column < 77:
                    char = '-'
                elif column == 77:
                    char = ':'
                elif 78 <= column < 80:
                    char = '-'
                elif 80 <= column < 82:
                    char = '='
                elif 82 <= column < 86:
                    char = '-'
                elif 86 <= column < 90:
                    char = ':'
                elif 90 <= column < 92:
                    char = '+'
                elif column == 92:
                    char = '='
                elif 93 <= column < 95:
                    char = '-'
                elif column == 95:
                    char = ':'
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 50:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 32:
                    char = '*'
                elif 32 <= column < 34:
                    char = '#'
                elif 34 <= column < 38:
                    char = '*'
                elif 38 <= column < 43:
                    char = '+'
                elif 43 <= column < 53:
                    char = '='
                elif 53 <= column < 62:
                    char = '+'
                elif 62 <= column < 72:
                    char = '*'
                elif column == 72:
                    char = '#'
                elif column == 73:
                    char = '*'
                elif column == 74:
                    char = '+'
                elif column == 75:
                    char = '='
                elif 76 <= column < 86:
                    char = '-'
                elif 86 <= column < 90:
                    char = ':'
                elif 90 <= column < 92:
                    char = '='
                elif 92 <= column < 94:
                    char = '-'
                elif column == 94:
                    char = ':'
                elif column == 95:
                    char = '-'
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 51:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 30:
                    char = '*'
                elif 30 <= column < 35:
                    char = '#'
                elif 35 <= column < 39:
                    char = '*'
                elif 39 <= column < 45:
                    char = '+'
                elif 45 <= column < 53:
                    char = '='
                elif 53 <= column < 56:
                    char = '+'
                elif 56 <= column < 61:
                    char = '*'
                elif 61 <= column < 64:
                    char = '#'
                elif 64 <= column < 67:
                    char = '*'
                elif column == 67:
                    char = '+'
                elif column == 68:
                    char = '='
                elif column == 69:
                    char = '-'
                elif 70 <= column < 72:
                    char = '='
                elif column == 72:
                    char = '+'
                elif column == 73:
                    char = '#'
                elif 74 <= column < 76:
                    char = '*'
                elif column == 76:
                    char = '+'
                elif 77 <= column < 79:
                    char = '='
                elif 79 <= column < 87:
                    char = '-'
                elif 87 <= column < 90:
                    char = ':'
                elif 90 <= column < 92:
                    char = '+'
                elif column == 92:
                    char = '='
                elif 93 <= column < 95:
                    char = '-'
                elif column == 95:
                    char = '+'
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '@'

            elif row == 52:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 17:
                    char = '*'
                elif 17 <= column < 19:
                    char = '+'
                elif 19 <= column < 22:
                    char = '='
                elif column == 22:
                    char = '-'
                elif 23 <= column < 30:
                    char = '='
                elif column == 30:
                    char = '*'
                elif 31 <= column < 35:
                    char = '#'
                elif 35 <= column < 42:
                    char = '*'
                elif 42 <= column < 46:
                    char = '+'
                elif 46 <= column < 52:
                    char = '='
                elif 52 <= column < 55:
                    char = '+'
                elif 55 <= column < 58:
                    char = '*'
                elif 58 <= column < 63:
                    char = '#'
                elif column == 63:
                    char = '*'
                elif column == 64:
                    char = '+'
                elif column == 65:
                    char = '='
                elif 66 <= column < 68:
                    char = '-'
                elif 68 <= column < 70:
                    char = ':'
                elif 70 <= column < 72:
                    char = '-'
                elif 72 <= column < 74:
                    char = '='
                elif column == 74:
                    char = '*'
                elif 75 <= column < 78:
                    char = '#'
                elif 78 <= column < 80:
                    char = '*'
                elif column == 80:
                    char = '+'
                elif 81 <= column < 87:
                    char = '='
                elif column == 87:
                    char = '-'
                elif column == 88:
                    char = ':'
                elif column == 89:
                    char = '-'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '+'
                elif column == 92:
                    char = '='
                elif column == 93:
                    char = '-'
                elif column == 94:
                    char = '+'
                elif 95 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif column == 117:
                    char = '%'
                elif 118 <= column < 120:
                    char = '@'

            elif row == 53:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif 12 <= column < 14:
                    char = '*'
                elif column == 14:
                    char = '+'
                elif column == 15:
                    char = '='
                elif column == 16:
                    char = '-'
                elif 17 <= column < 29:
                    char = ':'
                elif column == 29:
                    char = '-'
                elif column == 30:
                    char = '*'
                elif 31 <= column < 34:
                    char = '#'
                elif 34 <= column < 43:
                    char = '*'
                elif 43 <= column < 54:
                    char = '+'
                elif 54 <= column < 57:
                    char = '*'
                elif column == 57:
                    char = '#'
                elif 58 <= column < 62:
                    char = '*'
                elif column == 62:
                    char = '='
                elif 63 <= column < 65:
                    char = '-'
                elif 65 <= column < 69:
                    char = ':'
                elif 69 <= column < 73:
                    char = '-'
                elif 73 <= column < 76:
                    char = '='
                elif 76 <= column < 78:
                    char = '#'
                elif 78 <= column < 80:
                    char = '%'
                elif 80 <= column < 83:
                    char = '#'
                elif 83 <= column < 86:
                    char = '*'
                elif column == 86:
                    char = '+'
                elif column == 87:
                    char = '='
                elif column == 88:
                    char = '-'
                elif column == 89:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif column == 92:
                    char = '-'
                elif column == 93:
                    char = '+'
                elif 94 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 54:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 8:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif column == 11:
                    char = '+'
                elif column == 12:
                    char = '='
                elif column == 13:
                    char = '-'
                elif 14 <= column < 20:
                    char = ':'
                elif 20 <= column < 22:
                    char = '-'
                elif 22 <= column < 28:
                    char = ':'
                elif column == 28:
                    char = '-'
                elif column == 29:
                    char = '='
                elif 30 <= column < 34:
                    char = '#'
                elif 34 <= column < 46:
                    char = '*'
                elif 46 <= column < 53:
                    char = '+'
                elif 53 <= column < 57:
                    char = '*'
                elif 57 <= column < 59:
                    char = '+'
                elif 59 <= column < 61:
                    char = '*'
                elif 61 <= column < 63:
                    char = '+'
                elif column == 63:
                    char = '*'
                elif 64 <= column < 69:
                    char = '+'
                elif 69 <= column < 72:
                    char = '='
                elif 72 <= column < 75:
                    char = '+'
                elif column == 75:
                    char = '*'
                elif 76 <= column < 78:
                    char = '+'
                elif column == 78:
                    char = '*'
                elif column == 79:
                    char = '#'
                elif column == 80:
                    char = '*'
                elif column == 81:
                    char = '#'
                elif column == 82:
                    char = '+'
                elif 83 <= column < 86:
                    char = '='
                elif column == 86:
                    char = '-'
                elif column == 87:
                    char = '='
                elif column == 88:
                    char = '+'
                elif column == 89:
                    char = '*'
                elif column == 90:
                    char = '+'
                elif column == 91:
                    char = '-'
                elif column == 92:
                    char = '+'
                elif 93 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 55:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 8 <= column < 11:
                    char = '.'
                elif 11 <= column < 13:
                    char = ':'
                elif column == 13:
                    char = '-'
                elif 14 <= column < 17:
                    char = ':'
                elif 17 <= column < 19:
                    char = '-'
                elif 19 <= column < 27:
                    char = ':'
                elif column == 27:
                    char = '-'
                elif column == 28:
                    char = '+'
                elif 29 <= column < 33:
                    char = '#'
                elif 33 <= column < 46:
                    char = '*'
                elif 46 <= column < 53:
                    char = '+'
                elif 53 <= column < 56:
                    char = '*'
                elif 56 <= column < 59:
                    char = '+'
                elif column == 59:
                    char = '*'
                elif 60 <= column < 64:
                    char = '#'
                elif 64 <= column < 72:
                    char = '%'
                elif 72 <= column < 76:
                    char = '#'
                elif column == 76:
                    char = '*'
                elif column == 77:
                    char = '#'
                elif 78 <= column < 80:
                    char = '*'
                elif 80 <= column < 82:
                    char = '+'
                elif column == 82:
                    char = '='
                elif 83 <= column < 85:
                    char = '-'
                elif column == 85:
                    char = ':'
                elif column == 86:
                    char = '='
                elif 87 <= column < 89:
                    char = '+'
                elif column == 89:
                    char = '='
                elif column == 90:
                    char = '-'
                elif column == 91:
                    char = '+'
                elif 92 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 56:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 12:
                    char = '.'
                elif 12 <= column < 27:
                    char = ':'
                elif column == 27:
                    char = '='
                elif column == 28:
                    char = '*'
                elif 29 <= column < 33:
                    char = '#'
                elif 33 <= column < 46:
                    char = '*'
                elif 46 <= column < 50:
                    char = '+'
                elif column == 50:
                    char = '='
                elif 51 <= column < 53:
                    char = '+'
                elif 53 <= column < 63:
                    char = '*'
                elif 63 <= column < 69:
                    char = '+'
                elif 69 <= column < 72:
                    char = '*'
                elif 72 <= column < 76:
                    char = '#'
                elif column == 76:
                    char = '%'
                elif 77 <= column < 81:
                    char = '#'
                elif column == 81:
                    char = '%'
                elif 82 <= column < 86:
                    char = '#'
                elif column == 86:
                    char = '*'
                elif column == 87:
                    char = '='
                elif 88 <= column < 90:
                    char = '-'
                elif column == 90:
                    char = '+'
                elif 91 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 57:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 12:
                    char = '.'
                elif 12 <= column < 22:
                    char = ':'
                elif column == 22:
                    char = '.'
                elif 23 <= column < 26:
                    char = ':'
                elif column == 26:
                    char = '-'
                elif column == 27:
                    char = '+'
                elif column == 28:
                    char = '%'
                elif 29 <= column < 33:
                    char = '#'
                elif 33 <= column < 48:
                    char = '*'
                elif 48 <= column < 51:
                    char = '+'
                elif column == 51:
                    char = '='
                elif column == 52:
                    char = '+'
                elif 53 <= column < 58:
                    char = '*'
                elif column == 58:
                    char = '+'
                elif 59 <= column < 61:
                    char = '='
                elif column == 61:
                    char = '+'
                elif column == 62:
                    char = '*'
                elif 63 <= column < 65:
                    char = '+'
                elif 65 <= column < 67:
                    char = '='
                elif 67 <= column < 69:
                    char = '-'
                elif 69 <= column < 71:
                    char = '='
                elif 71 <= column < 73:
                    char = '+'
                elif 73 <= column < 75:
                    char = '='
                elif column == 75:
                    char = '+'
                elif 76 <= column < 82:
                    char = '*'
                elif column == 82:
                    char = '='
                elif column == 83:
                    char = '-'
                elif column == 84:
                    char = '+'
                elif column == 85:
                    char = '*'
                elif column == 86:
                    char = '+'
                elif column == 87:
                    char = '-'
                elif column == 88:
                    char = ':'
                elif 89 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 58:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 14:
                    char = ':'
                elif column == 14:
                    char = '-'
                elif 15 <= column < 19:
                    char = ':'
                elif 19 <= column < 24:
                    char = '.'
                elif 24 <= column < 26:
                    char = ':'
                elif column == 26:
                    char = '-'
                elif column == 27:
                    char = '*'
                elif column == 28:
                    char = '='
                elif column == 29:
                    char = '+'
                elif 30 <= column < 33:
                    char = '#'
                elif 33 <= column < 49:
                    char = '*'
                elif 49 <= column < 53:
                    char = '+'
                elif 53 <= column < 56:
                    char = '*'
                elif 56 <= column < 59:
                    char = '+'
                elif 59 <= column < 62:
                    char = '='
                elif 62 <= column < 66:
                    char = '+'
                elif 66 <= column < 71:
                    char = '='
                elif 71 <= column < 75:
                    char = '+'
                elif column == 75:
                    char = '='
                elif 76 <= column < 83:
                    char = '-'
                elif column == 83:
                    char = ':'
                elif column == 84:
                    char = '='
                elif column == 85:
                    char = '*'
                elif column == 86:
                    char = '='
                elif column == 87:
                    char = ':'
                elif column == 88:
                    char = '+'
                elif 89 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 59:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 18:
                    char = ':'
                elif 18 <= column < 23:
                    char = '.'
                elif 23 <= column < 25:
                    char = ':'
                elif column == 25:
                    char = '-'
                elif column == 26:
                    char = '+'
                elif column == 27:
                    char = '-'
                elif column == 28:
                    char = ':'
                elif 29 <= column < 32:
                    char = '#'
                elif 32 <= column < 50:
                    char = '*'
                elif 50 <= column < 54:
                    char = '+'
                elif 54 <= column < 56:
                    char = '*'
                elif 56 <= column < 59:
                    char = '+'
                elif 59 <= column < 65:
                    char = '='
                elif 65 <= column < 68:
                    char = '+'
                elif 68 <= column < 70:
                    char = '*'
                elif 70 <= column < 75:
                    char = '+'
                elif 75 <= column < 81:
                    char = '='
                elif column == 81:
                    char = '-'
                elif 82 <= column < 84:
                    char = ':'
                elif column == 84:
                    char = '='
                elif column == 85:
                    char = '+'
                elif column == 86:
                    char = '-'
                elif column == 87:
                    char = '+'
                elif 88 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif column == 116:
                    char = '@'
                elif 117 <= column < 120:
                    char = '%'

            elif row == 60:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 16:
                    char = ':'
                elif 16 <= column < 23:
                    char = '.'
                elif 23 <= column < 25:
                    char = ':'
                elif 25 <= column < 27:
                    char = '+'
                elif 27 <= column < 29:
                    char = ':'
                elif 29 <= column < 33:
                    char = '#'
                elif 33 <= column < 40:
                    char = '*'
                elif column == 40:
                    char = '+'
                elif 41 <= column < 57:
                    char = '*'
                elif 57 <= column < 61:
                    char = '+'
                elif 61 <= column < 64:
                    char = '='
                elif 64 <= column < 66:
                    char = '-'
                elif column == 66:
                    char = '='
                elif 67 <= column < 69:
                    char = '+'
                elif 69 <= column < 71:
                    char = '*'
                elif column == 71:
                    char = '#'
                elif 72 <= column < 79:
                    char = '*'
                elif 79 <= column < 81:
                    char = '+'
                elif column == 81:
                    char = '-'
                elif 82 <= column < 84:
                    char = ':'
                elif column == 84:
                    char = '='
                elif column == 85:
                    char = '-'
                elif column == 86:
                    char = '+'
                elif 87 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '%'

            elif row == 61:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 15:
                    char = ':'
                elif 15 <= column < 23:
                    char = '.'
                elif column == 23:
                    char = ':'
                elif 24 <= column < 27:
                    char = '-'
                elif column == 27:
                    char = ':'
                elif column == 28:
                    char = '.'
                elif column == 29:
                    char = ':'
                elif column == 30:
                    char = '*'
                elif column == 31:
                    char = '#'
                elif 32 <= column < 40:
                    char = '*'
                elif column == 40:
                    char = '+'
                elif 41 <= column < 60:
                    char = '*'
                elif 60 <= column < 63:
                    char = '+'
                elif 63 <= column < 66:
                    char = '='
                elif column == 66:
                    char = '-'
                elif 67 <= column < 69:
                    char = '='
                elif 69 <= column < 74:
                    char = '+'
                elif 74 <= column < 81:
                    char = '='
                elif 81 <= column < 84:
                    char = '-'
                elif column == 84:
                    char = '='
                elif column == 85:
                    char = '+'
                elif 86 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '%'

            elif row == 62:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 13:
                    char = ':'
                elif 13 <= column < 23:
                    char = '.'
                elif 23 <= column < 25:
                    char = '-'
                elif 25 <= column < 27:
                    char = ':'
                elif column == 27:
                    char = '-'
                elif column == 28:
                    char = ':'
                elif column == 29:
                    char = '.'
                elif column == 30:
                    char = ':'
                elif 31 <= column < 33:
                    char = '#'
                elif 33 <= column < 41:
                    char = '*'
                elif 41 <= column < 46:
                    char = '+'
                elif 46 <= column < 62:
                    char = '*'
                elif 62 <= column < 65:
                    char = '+'
                elif 65 <= column < 68:
                    char = '='
                elif 68 <= column < 72:
                    char = '-'
                elif 72 <= column < 75:
                    char = '='
                elif 75 <= column < 83:
                    char = '-'
                elif column == 83:
                    char = '='
                elif 84 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '*'
                elif 116 <= column < 120:
                    char = '%'

            elif row == 63:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 12:
                    char = '.'
                elif column == 12:
                    char = ':'
                elif 13 <= column < 22:
                    char = '.'
                elif column == 22:
                    char = ':'
                elif column == 23:
                    char = '='
                elif 24 <= column < 27:
                    char = ':'
                elif 27 <= column < 29:
                    char = '-'
                elif column == 29:
                    char = ':'
                elif column == 30:
                    char = '.'
                elif column == 31:
                    char = '-'
                elif column == 32:
                    char = '#'
                elif 33 <= column < 41:
                    char = '*'
                elif 41 <= column < 43:
                    char = '+'
                elif 43 <= column < 53:
                    char = '*'
                elif 53 <= column < 61:
                    char = '#'
                elif 61 <= column < 65:
                    char = '*'
                elif 65 <= column < 68:
                    char = '+'
                elif 68 <= column < 76:
                    char = '='
                elif 76 <= column < 82:
                    char = '-'
                elif column == 82:
                    char = ':'
                elif column == 83:
                    char = '-'
                elif column == 84:
                    char = '='
                elif column == 85:
                    char = '+'
                elif 86 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '%'

            elif row == 64:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 21:
                    char = '.'
                elif column == 21:
                    char = ':'
                elif 22 <= column < 25:
                    char = '-'
                elif column == 25:
                    char = ':'
                elif column == 26:
                    char = '.'
                elif column == 27:
                    char = ':'
                elif column == 28:
                    char = '-'
                elif 29 <= column < 31:
                    char = ':'
                elif column == 31:
                    char = '.'
                elif column == 32:
                    char = '-'
                elif column == 33:
                    char = '#'
                elif 34 <= column < 49:
                    char = '*'
                elif 49 <= column < 51:
                    char = '+'
                elif 51 <= column < 55:
                    char = '*'
                elif 55 <= column < 65:
                    char = '#'
                elif 65 <= column < 69:
                    char = '*'
                elif 69 <= column < 75:
                    char = '+'
                elif 75 <= column < 80:
                    char = '='
                elif column == 80:
                    char = '-'
                elif 81 <= column < 84:
                    char = ':'
                elif 84 <= column < 86:
                    char = '.'
                elif column == 86:
                    char = ':'
                elif column == 87:
                    char = '-'
                elif column == 88:
                    char = '='
                elif column == 89:
                    char = '+'
                elif 90 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '%'

            elif row == 65:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 21:
                    char = '.'
                elif column == 21:
                    char = ':'
                elif column == 22:
                    char = '-'
                elif column == 23:
                    char = ':'
                elif column == 24:
                    char = '-'
                elif column == 25:
                    char = ':'
                elif 26 <= column < 28:
                    char = '.'
                elif 28 <= column < 30:
                    char = '-'
                elif 30 <= column < 32:
                    char = ':'
                elif column == 32:
                    char = '.'
                elif column == 33:
                    char = '='
                elif column == 34:
                    char = '#'
                elif 35 <= column < 59:
                    char = '*'
                elif 59 <= column < 71:
                    char = '#'
                elif 71 <= column < 77:
                    char = '*'
                elif 77 <= column < 80:
                    char = '+'
                elif column == 80:
                    char = '='
                elif 81 <= column < 83:
                    char = '.'
                elif column == 83:
                    char = ':'
                elif column == 84:
                    char = '-'
                elif column == 85:
                    char = ':'
                elif 86 <= column < 90:
                    char = '.'
                elif column == 90:
                    char = '-'
                elif column == 91:
                    char = '+'
                elif 92 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif column == 116:
                    char = '%'
                elif column == 117:
                    char = '#'
                elif column == 118:
                    char = '%'
                elif column == 119:
                    char = '#'

            elif row == 66:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 20:
                    char = '.'
                elif column == 20:
                    char = ':'
                elif column == 21:
                    char = '-'
                elif 22 <= column < 29:
                    char = ':'
                elif 29 <= column < 31:
                    char = '-'
                elif 31 <= column < 33:
                    char = ':'
                elif column == 33:
                    char = '.'
                elif column == 34:
                    char = '+'
                elif column == 35:
                    char = '#'
                elif 36 <= column < 53:
                    char = '*'
                elif 53 <= column < 56:
                    char = '+'
                elif 56 <= column < 59:
                    char = '*'
                elif 59 <= column < 67:
                    char = '#'
                elif 67 <= column < 69:
                    char = '*'
                elif 69 <= column < 72:
                    char = '+'
                elif 72 <= column < 75:
                    char = '*'
                elif column == 75:
                    char = '#'
                elif 76 <= column < 79:
                    char = '*'
                elif 79 <= column < 81:
                    char = '+'
                elif column == 81:
                    char = '-'
                elif 82 <= column < 84:
                    char = '.'
                elif column == 84:
                    char = ':'
                elif column == 85:
                    char = '-'
                elif column == 86:
                    char = ':'
                elif 87 <= column < 92:
                    char = '.'
                elif column == 92:
                    char = ':'
                elif column == 93:
                    char = '='
                elif 94 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif column == 116:
                    char = '%'
                elif 117 <= column < 120:
                    char = '#'

            elif row == 67:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 20:
                    char = '.'
                elif column == 20:
                    char = ':'
                elif column == 21:
                    char = '-'
                elif 22 <= column < 25:
                    char = ':'
                elif column == 25:
                    char = '.'
                elif 26 <= column < 29:
                    char = ':'
                elif column == 29:
                    char = '.'
                elif column == 30:
                    char = ':'
                elif column == 31:
                    char = '-'
                elif column == 32:
                    char = ':'
                elif column == 33:
                    char = '.'
                elif column == 34:
                    char = ':'
                elif 35 <= column < 39:
                    char = '*'
                elif column == 39:
                    char = '+'
                elif 40 <= column < 56:
                    char = '*'
                elif column == 56:
                    char = '#'
                elif 57 <= column < 62:
                    char = '*'
                elif 62 <= column < 65:
                    char = '#'
                elif column == 65:
                    char = '*'
                elif column == 66:
                    char = '='
                elif 67 <= column < 71:
                    char = ':'
                elif 71 <= column < 73:
                    char = '-'
                elif column == 73:
                    char = '='
                elif column == 74:
                    char = '+'
                elif 75 <= column < 77:
                    char = '*'
                elif 77 <= column < 80:
                    char = '#'
                elif 80 <= column < 82:
                    char = '*'
                elif column == 82:
                    char = ':'
                elif column == 83:
                    char = '.'
                elif 84 <= column < 86:
                    char = ':'
                elif column == 86:
                    char = '-'
                elif column == 87:
                    char = ':'
                elif 88 <= column < 94:
                    char = '.'
                elif column == 94:
                    char = ':'
                elif column == 95:
                    char = '+'
                elif 96 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif column == 116:
                    char = '%'
                elif 117 <= column < 120:
                    char = '#'

            elif row == 68:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 18:
                    char = '.'
                elif column == 18:
                    char = ':'
                elif column == 19:
                    char = '.'
                elif 20 <= column < 25:
                    char = ':'
                elif 25 <= column < 27:
                    char = '.'
                elif 27 <= column < 30:
                    char = ':'
                elif column == 30:
                    char = '.'
                elif column == 31:
                    char = ':'
                elif column == 32:
                    char = '-'
                elif column == 33:
                    char = ':'
                elif column == 34:
                    char = '.'
                elif column == 35:
                    char = '-'
                elif 36 <= column < 39:
                    char = '*'
                elif 39 <= column < 43:
                    char = '+'
                elif 43 <= column < 48:
                    char = '*'
                elif 48 <= column < 50:
                    char = '+'
                elif 50 <= column < 62:
                    char = '*'
                elif column == 62:
                    char = '#'
                elif 63 <= column < 65:
                    char = '*'
                elif column == 65:
                    char = '-'
                elif 66 <= column < 69:
                    char = ':'
                elif 69 <= column < 73:
                    char = '-'
                elif 73 <= column < 75:
                    char = '='
                elif column == 75:
                    char = '+'
                elif 76 <= column < 80:
                    char = '*'
                elif 80 <= column < 82:
                    char = '#'
                elif column == 82:
                    char = '+'
                elif column == 83:
                    char = '.'
                elif 84 <= column < 89:
                    char = ':'
                elif 89 <= column < 96:
                    char = '.'
                elif column == 96:
                    char = ':'
                elif column == 97:
                    char = '='
                elif column == 98:
                    char = '+'
                elif 99 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif column == 116:
                    char = '%'
                elif 117 <= column < 120:
                    char = '#'

            elif row == 69:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 20:
                    char = '.'
                elif column == 20:
                    char = ':'
                elif column == 21:
                    char = '-'
                elif 22 <= column < 26:
                    char = ':'
                elif 26 <= column < 29:
                    char = '.'
                elif 29 <= column < 32:
                    char = ':'
                elif column == 32:
                    char = '.'
                elif 33 <= column < 35:
                    char = ':'
                elif column == 35:
                    char = '.'
                elif column == 36:
                    char = '+'
                elif 37 <= column < 40:
                    char = '*'
                elif 40 <= column < 49:
                    char = '+'
                elif 49 <= column < 63:
                    char = '*'
                elif column == 63:
                    char = '='
                elif 64 <= column < 71:
                    char = '-'
                elif 71 <= column < 76:
                    char = '='
                elif 76 <= column < 78:
                    char = '+'
                elif 78 <= column < 83:
                    char = '*'
                elif column == 83:
                    char = '='
                elif column == 84:
                    char = '.'
                elif 85 <= column < 88:
                    char = ':'
                elif column == 88:
                    char = '.'
                elif column == 89:
                    char = ':'
                elif 90 <= column < 98:
                    char = '.'
                elif 98 <= column < 100:
                    char = ':'
                elif column == 100:
                    char = '-'
                elif column == 101:
                    char = '='
                elif 102 <= column < 104:
                    char = '+'
                elif 104 <= column < 108:
                    char = '*'
                elif column == 108:
                    char = '+'
                elif 109 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif column == 116:
                    char = '%'
                elif 117 <= column < 120:
                    char = '#'

            elif row == 70:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 20:
                    char = '.'
                elif 20 <= column < 22:
                    char = ':'
                elif column == 22:
                    char = '-'
                elif 23 <= column < 26:
                    char = ':'
                elif 26 <= column < 30:
                    char = '.'
                elif 30 <= column < 34:
                    char = ':'
                elif column == 34:
                    char = '.'
                elif 35 <= column < 37:
                    char = ':'
                elif 37 <= column < 39:
                    char = '*'
                elif 39 <= column < 42:
                    char = '+'
                elif 42 <= column < 45:
                    char = '='
                elif column == 45:
                    char = '+'
                elif 46 <= column < 54:
                    char = '*'
                elif 54 <= column < 56:
                    char = '+'
                elif 56 <= column < 62:
                    char = '*'
                elif 62 <= column < 64:
                    char = '+'
                elif 64 <= column < 76:
                    char = '='
                elif 76 <= column < 80:
                    char = '+'
                elif 80 <= column < 84:
                    char = '*'
                elif column == 84:
                    char = '-'
                elif 85 <= column < 87:
                    char = ':'
                elif column == 87:
                    char = '-'
                elif column == 88:
                    char = '.'
                elif 89 <= column < 91:
                    char = ':'
                elif 91 <= column < 95:
                    char = '.'
                elif column == 95:
                    char = ':'
                elif 96 <= column < 104:
                    char = '.'
                elif column == 104:
                    char = ':'
                elif column == 105:
                    char = '-'
                elif 106 <= column < 109:
                    char = '='
                elif 109 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif column == 116:
                    char = '%'
                elif 117 <= column < 120:
                    char = '#'

            elif row == 71:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 19:
                    char = '.'
                elif 19 <= column < 23:
                    char = ':'
                elif column == 23:
                    char = '-'
                elif 24 <= column < 26:
                    char = ':'
                elif 26 <= column < 33:
                    char = '.'
                elif 33 <= column < 35:
                    char = ':'
                elif 35 <= column < 37:
                    char = '.'
                elif column == 37:
                    char = ':'
                elif column == 38:
                    char = '='
                elif 39 <= column < 45:
                    char = '+'
                elif 45 <= column < 47:
                    char = '*'
                elif 47 <= column < 50:
                    char = '+'
                elif 50 <= column < 53:
                    char = '='
                elif 53 <= column < 57:
                    char = '+'
                elif 57 <= column < 59:
                    char = '*'
                elif 59 <= column < 65:
                    char = '+'
                elif 65 <= column < 67:
                    char = '='
                elif 67 <= column < 72:
                    char = '-'
                elif 72 <= column < 81:
                    char = '='
                elif 81 <= column < 83:
                    char = '+'
                elif 83 <= column < 85:
                    char = '*'
                elif column == 85:
                    char = '-'
                elif column == 86:
                    char = ':'
                elif column == 87:
                    char = '-'
                elif 88 <= column < 90:
                    char = '.'
                elif 90 <= column < 92:
                    char = ':'
                elif 92 <= column < 100:
                    char = '.'
                elif column == 100:
                    char = ':'
                elif 101 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '#'

            elif row == 72:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 18:
                    char = '.'
                elif 18 <= column < 22:
                    char = ':'
                elif column == 22:
                    char = '.'
                elif 23 <= column < 25:
                    char = ':'
                elif column == 25:
                    char = '-'
                elif 26 <= column < 28:
                    char = ':'
                elif column == 28:
                    char = '.'
                elif column == 29:
                    char = ':'
                elif 30 <= column < 35:
                    char = '.'
                elif 35 <= column < 37:
                    char = ':'
                elif 37 <= column < 39:
                    char = '.'
                elif column == 39:
                    char = ':'
                elif column == 40:
                    char = '='
                elif 41 <= column < 46:
                    char = '+'
                elif 46 <= column < 49:
                    char = '='
                elif 49 <= column < 52:
                    char = '-'
                elif 52 <= column < 56:
                    char = '='
                elif 56 <= column < 63:
                    char = '+'
                elif 63 <= column < 67:
                    char = '='
                elif 67 <= column < 81:
                    char = '-'
                elif 81 <= column < 83:
                    char = '='
                elif column == 83:
                    char = '+'
                elif 84 <= column < 86:
                    char = '*'
                elif 86 <= column < 88:
                    char = ':'
                elif 88 <= column < 90:
                    char = '.'
                elif 90 <= column < 92:
                    char = ':'
                elif 92 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '#'

            elif row == 73:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 18:
                    char = '.'
                elif 18 <= column < 21:
                    char = ':'
                elif 21 <= column < 25:
                    char = '.'
                elif column == 25:
                    char = ':'
                elif column == 26:
                    char = '-'
                elif 27 <= column < 30:
                    char = ':'
                elif 30 <= column < 37:
                    char = '.'
                elif 37 <= column < 40:
                    char = ':'
                elif column == 40:
                    char = '.'
                elif column == 41:
                    char = ':'
                elif column == 42:
                    char = '='
                elif 43 <= column < 45:
                    char = '+'
                elif column == 45:
                    char = '='
                elif 46 <= column < 54:
                    char = '-'
                elif 54 <= column < 57:
                    char = '='
                elif column == 57:
                    char = '+'
                elif 58 <= column < 66:
                    char = '='
                elif 66 <= column < 81:
                    char = '-'
                elif 81 <= column < 83:
                    char = '='
                elif column == 83:
                    char = '+'
                elif 84 <= column < 86:
                    char = '*'
                elif column == 86:
                    char = '+'
                elif column == 87:
                    char = ':'
                elif 88 <= column < 90:
                    char = '.'
                elif 90 <= column < 93:
                    char = ':'
                elif 93 <= column < 97:
                    char = '.'
                elif column == 97:
                    char = ':'
                elif 98 <= column < 101:
                    char = '.'
                elif column == 101:
                    char = ':'
                elif 102 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '#'

            elif row == 74:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 18:
                    char = '.'
                elif 18 <= column < 22:
                    char = ':'
                elif 22 <= column < 26:
                    char = '.'
                elif 26 <= column < 28:
                    char = ':'
                elif column == 28:
                    char = '-'
                elif 29 <= column < 32:
                    char = ':'
                elif 32 <= column < 40:
                    char = '.'
                elif 40 <= column < 42:
                    char = ':'
                elif column == 42:
                    char = '.'
                elif column == 43:
                    char = ':'
                elif column == 44:
                    char = '-'
                elif 45 <= column < 48:
                    char = '='
                elif 48 <= column < 53:
                    char = '-'
                elif 53 <= column < 61:
                    char = '='
                elif 61 <= column < 71:
                    char = '-'
                elif 71 <= column < 78:
                    char = '='
                elif 78 <= column < 83:
                    char = '-'
                elif column == 83:
                    char = '='
                elif column == 84:
                    char = '+'
                elif 85 <= column < 87:
                    char = '*'
                elif column == 87:
                    char = '='
                elif 88 <= column < 91:
                    char = '.'
                elif 91 <= column < 94:
                    char = ':'
                elif 94 <= column < 102:
                    char = '.'
                elif column == 102:
                    char = ':'
                elif 103 <= column < 110:
                    char = '.'
                elif column == 111:
                    char = '.'
                elif column == 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '#'

            elif row == 75:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 17:
                    char = '.'
                elif column == 17:
                    char = ':'
                elif column == 18:
                    char = '-'
                elif 19 <= column < 23:
                    char = ':'
                elif 23 <= column < 28:
                    char = '.'
                elif 28 <= column < 33:
                    char = ':'
                elif 33 <= column < 41:
                    char = '.'
                elif 41 <= column < 43:
                    char = ':'
                elif 43 <= column < 45:
                    char = '.'
                elif column == 45:
                    char = ':'
                elif column == 46:
                    char = '-'
                elif 47 <= column < 49:
                    char = '+'
                elif 49 <= column < 60:
                    char = '='
                elif 60 <= column < 83:
                    char = '-'
                elif 83 <= column < 85:
                    char = '='
                elif column == 85:
                    char = '+'
                elif column == 86:
                    char = '*'
                elif column == 87:
                    char = '+'
                elif 88 <= column < 91:
                    char = '.'
                elif 91 <= column < 94:
                    char = ':'
                elif 94 <= column < 102:
                    char = '.'
                elif 102 <= column < 104:
                    char = ':'
                elif 104 <= column < 110:
                    char = '.'
                elif column == 111:
                    char = '.'
                elif column == 113:
                    char = '.'
                elif column == 115:
                    char = '+'
                elif 116 <= column < 120:
                    char = '#'

            elif row == 76:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 16:
                    char = '.'
                elif column == 16:
                    char = ':'
                elif column == 17:
                    char = '-'
                elif 18 <= column < 24:
                    char = ':'
                elif 24 <= column < 30:
                    char = '.'
                elif 30 <= column < 34:
                    char = ':'
                elif 34 <= column < 42:
                    char = '.'
                elif 42 <= column < 45:
                    char = ':'
                elif 45 <= column < 47:
                    char = '.'
                elif column == 47:
                    char = ':'
                elif column == 48:
                    char = '-'
                elif 49 <= column < 51:
                    char = '+'
                elif 51 <= column < 59:
                    char = '='
                elif 59 <= column < 66:
                    char = '-'
                elif 66 <= column < 80:
                    char = ':'
                elif 80 <= column < 84:
                    char = '-'
                elif column == 84:
                    char = '='
                elif 85 <= column < 88:
                    char = '+'
                elif column == 88:
                    char = ':'
                elif 89 <= column < 93:
                    char = '.'
                elif 93 <= column < 95:
                    char = ':'
                elif 95 <= column < 104:
                    char = '.'
                elif column == 104:
                    char = ':'
                elif 105 <= column < 112:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '#'

            elif row == 77:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 16:
                    char = '.'
                elif column == 16:
                    char = ':'
                elif column == 17:
                    char = '-'
                elif 18 <= column < 20:
                    char = ':'
                elif 20 <= column < 22:
                    char = '.'
                elif 22 <= column < 25:
                    char = ':'
                elif 25 <= column < 32:
                    char = '.'
                elif 32 <= column < 36:
                    char = ':'
                elif 36 <= column < 44:
                    char = '.'
                elif 44 <= column < 47:
                    char = ':'
                elif 47 <= column < 49:
                    char = '.'
                elif column == 49:
                    char = ':'
                elif column == 50:
                    char = '='
                elif column == 51:
                    char = '+'
                elif 52 <= column < 54:
                    char = '='
                elif 54 <= column < 65:
                    char = '-'
                elif 65 <= column < 80:
                    char = ':'
                elif 80 <= column < 84:
                    char = '-'
                elif 84 <= column < 86:
                    char = '='
                elif column == 86:
                    char = '+'
                elif column == 87:
                    char = '*'
                elif column == 88:
                    char = '-'
                elif 89 <= column < 94:
                    char = '.'
                elif 94 <= column < 96:
                    char = ':'
                elif 96 <= column < 104:
                    char = '.'
                elif 104 <= column < 106:
                    char = ':'
                elif 106 <= column < 112:
                    char = '.'
                elif column == 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '#'
                elif 117 <= column < 119:
                    char = '*'
                elif column == 119:
                    char = '#'

            elif row == 78:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 15:
                    char = '.'
                elif 15 <= column < 17:
                    char = ':'
                elif column == 17:
                    char = '-'
                elif 18 <= column < 20:
                    char = ':'
                elif 20 <= column < 24:
                    char = '.'
                elif 24 <= column < 26:
                    char = ':'
                elif 26 <= column < 33:
                    char = '.'
                elif 33 <= column < 38:
                    char = ':'
                elif 38 <= column < 48:
                    char = '.'
                elif column == 48:
                    char = ':'
                elif 49 <= column < 51:
                    char = '.'
                elif column == 51:
                    char = '-'
                elif column == 52:
                    char = '+'
                elif column == 53:
                    char = '='
                elif 54 <= column < 64:
                    char = '-'
                elif 64 <= column < 81:
                    char = ':'
                elif 81 <= column < 85:
                    char = '-'
                elif column == 85:
                    char = '='
                elif 86 <= column < 88:
                    char = '+'
                elif column == 88:
                    char = '='
                elif 89 <= column < 95:
                    char = '.'
                elif column == 95:
                    char = ':'
                elif 96 <= column < 105:
                    char = '.'
                elif column == 105:
                    char = ':'
                elif 106 <= column < 112:
                    char = '.'
                elif column == 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '#'
                elif 117 <= column < 120:
                    char = '*'

            elif row == 79:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 14:
                    char = '.'
                elif 14 <= column < 17:
                    char = ':'
                elif column == 17:
                    char = '-'
                elif 18 <= column < 20:
                    char = ':'
                elif 20 <= column < 25:
                    char = '.'
                elif 25 <= column < 28:
                    char = ':'
                elif 28 <= column < 36:
                    char = '.'
                elif 36 <= column < 39:
                    char = ':'
                elif 39 <= column < 49:
                    char = '.'
                elif 49 <= column < 51:
                    char = ':'
                elif column == 51:
                    char = '.'
                elif column == 52:
                    char = ':'
                elif 53 <= column < 56:
                    char = '='
                elif 56 <= column < 66:
                    char = '-'
                elif 66 <= column < 82:
                    char = ':'
                elif 82 <= column < 85:
                    char = '-'
                elif 85 <= column < 87:
                    char = '='
                elif 87 <= column < 89:
                    char = '+'
                elif column == 89:
                    char = ':'
                elif 90 <= column < 95:
                    char = '.'
                elif 95 <= column < 97:
                    char = ':'
                elif 97 <= column < 111:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '#'
                elif 117 <= column < 120:
                    char = '*'

            elif row == 80:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 13:
                    char = '.'
                elif 13 <= column < 17:
                    char = ':'
                elif column == 17:
                    char = '-'
                elif 18 <= column < 20:
                    char = ':'
                elif 20 <= column < 27:
                    char = '.'
                elif 27 <= column < 29:
                    char = ':'
                elif 29 <= column < 37:
                    char = '.'
                elif 37 <= column < 40:
                    char = ':'
                elif 40 <= column < 54:
                    char = '.'
                elif column == 54:
                    char = ':'
                elif 55 <= column < 57:
                    char = '='
                elif 57 <= column < 59:
                    char = '-'
                elif 59 <= column < 61:
                    char = '='
                elif 61 <= column < 66:
                    char = '-'
                elif 66 <= column < 80:
                    char = ':'
                elif 80 <= column < 85:
                    char = '-'
                elif 85 <= column < 87:
                    char = '='
                elif 87 <= column < 90:
                    char = '+'
                elif column == 90:
                    char = ':'
                elif 91 <= column < 96:
                    char = '.'
                elif column == 96:
                    char = ':'
                elif 97 <= column < 111:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '#'
                elif 117 <= column < 120:
                    char = '*'

            elif row == 81:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 13:
                    char = '.'
                elif 13 <= column < 17:
                    char = ':'
                elif column == 17:
                    char = '-'
                elif 18 <= column < 21:
                    char = ':'
                elif 21 <= column < 28:
                    char = '.'
                elif 28 <= column < 30:
                    char = ':'
                elif 30 <= column < 39:
                    char = '.'
                elif 39 <= column < 42:
                    char = ':'
                elif 42 <= column < 52:
                    char = '.'
                elif 52 <= column < 54:
                    char = ':'
                elif column == 54:
                    char = '.'
                elif column == 55:
                    char = ':'
                elif 56 <= column < 59:
                    char = '='
                elif column == 59:
                    char = '-'
                elif column == 60:
                    char = '='
                elif 61 <= column < 66:
                    char = '-'
                elif 66 <= column < 70:
                    char = ':'
                elif 70 <= column < 86:
                    char = '-'
                elif 86 <= column < 88:
                    char = '='
                elif 88 <= column < 90:
                    char = '+'
                elif column == 90:
                    char = '='
                elif 91 <= column < 97:
                    char = '.'
                elif column == 97:
                    char = ':'
                elif 98 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '#'
                elif 117 <= column < 120:
                    char = '*'

            elif row == 82:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 12:
                    char = '.'
                elif 12 <= column < 16:
                    char = ':'
                elif 16 <= column < 18:
                    char = '-'
                elif 18 <= column < 20:
                    char = ':'
                elif 20 <= column < 29:
                    char = '.'
                elif 29 <= column < 32:
                    char = ':'
                elif 32 <= column < 41:
                    char = '.'
                elif 41 <= column < 44:
                    char = ':'
                elif 44 <= column < 53:
                    char = '.'
                elif 53 <= column < 55:
                    char = ':'
                elif 55 <= column < 57:
                    char = '.'
                elif column == 57:
                    char = '-'
                elif 58 <= column < 60:
                    char = '='
                elif 60 <= column < 67:
                    char = '-'
                elif 67 <= column < 69:
                    char = ':'
                elif 69 <= column < 86:
                    char = '-'
                elif 86 <= column < 88:
                    char = '='
                elif 88 <= column < 91:
                    char = '+'
                elif column == 91:
                    char = '-'
                elif 92 <= column < 98:
                    char = '.'
                elif column == 98:
                    char = ':'
                elif 99 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '#'
                elif 117 <= column < 120:
                    char = '*'

            elif row == 83:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 16:
                    char = ':'
                elif 16 <= column < 18:
                    char = '-'
                elif 18 <= column < 21:
                    char = ':'
                elif 21 <= column < 31:
                    char = '.'
                elif 31 <= column < 34:
                    char = ':'
                elif 34 <= column < 56:
                    char = '.'
                elif column == 56:
                    char = ':'
                elif column == 57:
                    char = '.'
                elif column == 58:
                    char = ':'
                elif 59 <= column < 62:
                    char = '='
                elif 62 <= column < 71:
                    char = '-'
                elif column == 71:
                    char = ':'
                elif 72 <= column < 77:
                    char = '-'
                elif 77 <= column < 83:
                    char = ':'
                elif 83 <= column < 86:
                    char = '-'
                elif 86 <= column < 89:
                    char = '='
                elif column == 89:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif 92 <= column < 111:
                    char = '.'
                elif column == 112:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 84:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 16:
                    char = ':'
                elif column == 16:
                    char = '-'
                elif 17 <= column < 22:
                    char = ':'
                elif 22 <= column < 32:
                    char = '.'
                elif 32 <= column < 35:
                    char = ':'
                elif 35 <= column < 39:
                    char = '.'
                elif column == 39:
                    char = ':'
                elif 40 <= column < 45:
                    char = '.'
                elif 45 <= column < 47:
                    char = ':'
                elif 47 <= column < 60:
                    char = '.'
                elif column == 60:
                    char = '-'
                elif 61 <= column < 63:
                    char = '='
                elif 63 <= column < 70:
                    char = '-'
                elif 70 <= column < 81:
                    char = ':'
                elif 81 <= column < 86:
                    char = '-'
                elif 86 <= column < 89:
                    char = '='
                elif column == 89:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif 92 <= column < 99:
                    char = '.'
                elif column == 99:
                    char = ':'
                elif 100 <= column < 111:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 85:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 16:
                    char = ':'
                elif column == 16:
                    char = '-'
                elif 17 <= column < 22:
                    char = ':'
                elif 22 <= column < 34:
                    char = '.'
                elif 34 <= column < 37:
                    char = ':'
                elif 37 <= column < 39:
                    char = '.'
                elif 39 <= column < 41:
                    char = ':'
                elif 41 <= column < 57:
                    char = '.'
                elif 57 <= column < 59:
                    char = ':'
                elif 59 <= column < 62:
                    char = '.'
                elif column == 62:
                    char = '-'
                elif 63 <= column < 65:
                    char = '='
                elif 65 <= column < 76:
                    char = '-'
                elif 76 <= column < 78:
                    char = ':'
                elif 78 <= column < 86:
                    char = '-'
                elif 86 <= column < 89:
                    char = '='
                elif column == 89:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif 92 <= column < 99:
                    char = '.'
                elif column == 99:
                    char = ':'
                elif 100 <= column < 110:
                    char = '.'
                elif 111 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 86:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 16:
                    char = ':'
                elif column == 16:
                    char = '-'
                elif 17 <= column < 23:
                    char = ':'
                elif 23 <= column < 36:
                    char = '.'
                elif 36 <= column < 39:
                    char = ':'
                elif column == 39:
                    char = '.'
                elif 40 <= column < 44:
                    char = ':'
                elif 44 <= column < 60:
                    char = '.'
                elif column == 60:
                    char = ':'
                elif 61 <= column < 63:
                    char = '.'
                elif column == 63:
                    char = ':'
                elif column == 64:
                    char = '='
                elif column == 65:
                    char = '+'
                elif column == 66:
                    char = '='
                elif 67 <= column < 86:
                    char = '-'
                elif 86 <= column < 89:
                    char = '='
                elif column == 89:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif 92 <= column < 100:
                    char = '.'
                elif column == 100:
                    char = ':'
                elif 101 <= column < 110:
                    char = '.'
                elif 111 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 87:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 24:
                    char = ':'
                elif 24 <= column < 36:
                    char = '.'
                elif 36 <= column < 40:
                    char = ':'
                elif column == 40:
                    char = '.'
                elif 41 <= column < 45:
                    char = ':'
                elif 45 <= column < 50:
                    char = '.'
                elif column == 50:
                    char = ':'
                elif 51 <= column < 62:
                    char = '.'
                elif column == 62:
                    char = ':'
                elif 63 <= column < 65:
                    char = '.'
                elif column == 65:
                    char = ':'
                elif 66 <= column < 70:
                    char = '='
                elif 70 <= column < 85:
                    char = '-'
                elif 85 <= column < 89:
                    char = '='
                elif column == 89:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif 92 <= column < 100:
                    char = '.'
                elif column == 100:
                    char = ':'
                elif 101 <= column < 110:
                    char = '.'
                elif 111 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 88:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 10:
                    char = '.'
                elif 11 <= column < 16:
                    char = ':'
                elif column == 16:
                    char = '-'
                elif 17 <= column < 24:
                    char = ':'
                elif 24 <= column < 38:
                    char = '.'
                elif 38 <= column < 47:
                    char = ':'
                elif 47 <= column < 62:
                    char = '.'
                elif 62 <= column < 65:
                    char = ':'
                elif column == 65:
                    char = '.'
                elif column == 66:
                    char = ':'
                elif column == 67:
                    char = '='
                elif column == 68:
                    char = '+'
                elif 69 <= column < 73:
                    char = '='
                elif 73 <= column < 83:
                    char = '-'
                elif 83 <= column < 88:
                    char = '='
                elif 88 <= column < 90:
                    char = '+'
                elif column == 90:
                    char = '*'
                elif column == 91:
                    char = '='
                elif 92 <= column < 101:
                    char = '.'
                elif column == 101:
                    char = ':'
                elif 102 <= column < 110:
                    char = '.'
                elif 111 <= column < 114:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 89:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 10 <= column < 14:
                    char = '.'
                elif 14 <= column < 24:
                    char = ':'
                elif 24 <= column < 40:
                    char = '.'
                elif 40 <= column < 42:
                    char = ':'
                elif 42 <= column < 45:
                    char = '.'
                elif 45 <= column < 47:
                    char = ':'
                elif 47 <= column < 65:
                    char = '.'
                elif column == 65:
                    char = ':'
                elif 66 <= column < 68:
                    char = '.'
                elif column == 68:
                    char = '-'
                elif 69 <= column < 72:
                    char = '='
                elif 72 <= column < 85:
                    char = '-'
                elif 85 <= column < 90:
                    char = '='
                elif column == 90:
                    char = '+'
                elif column == 91:
                    char = '-'
                elif 92 <= column < 110:
                    char = '.'
                elif 111 <= column < 113:
                    char = '.'
                elif column == 115:
                    char = '='
                elif 116 <= column < 120:
                    char = '*'

            elif row == 90:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif 9 <= column < 68:
                    char = '.'
                elif 69 <= column < 107:
                    char = '.'
                elif 108 <= column < 110:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '*'
                elif column == 117:
                    char = '+'
                elif 118 <= column < 120:
                    char = '*'

            elif row == 91:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 9:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '*'
                elif column == 117:
                    char = '+'
                elif 118 <= column < 120:
                    char = '*'

            elif row == 92:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '#'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '.'
                elif column == 115:
                    char = '='
                elif column == 116:
                    char = '*'
                elif column == 117:
                    char = '+'
                elif 118 <= column < 120:
                    char = '*'

            elif row == 93:
                if 0 <= column < 4:
                    char = '@'
                elif column == 4:
                    char = '*'
                elif 5 <= column < 7:
                    char = '='
                elif 7 <= column < 9:
                    char = '-'
                elif column == 9:
                    char = '='
                elif column == 10:
                    char = '-'
                elif 11 <= column < 37:
                    char = '='
                elif 37 <= column < 115:
                    char = '+'
                elif 115 <= column < 117:
                    char = '*'
                elif column == 117:
                    char = '+'
                elif 118 <= column < 120:
                    char = '*'

            elif row == 94:
                if 0 <= column < 2:
                    char = '@'
                elif column == 2:
                    char = '#'
                elif column == 3:
                    char = '*'
                elif column == 4:
                    char = '+'
                elif 5 <= column < 18:
                    char = '*'
                elif 18 <= column < 33:
                    char = '#'
                elif 33 <= column < 47:
                    char = '%'
                elif 47 <= column < 116:
                    char = '@'
                elif column == 116:
                    char = '%'
                elif column == 117:
                    char = '*'
                elif column == 118:
                    char = '+'
                elif column == 119:
                    char = '*'

            elif row == 95:
                if column == 0:
                    char = '#'
                elif column == 1:
                    char = '*'
                elif 2 <= column < 4:
                    char = '+'
                elif 4 <= column < 8:
                    char = '*'
                elif column == 8:
                    char = '+'
                elif 9 <= column < 23:
                    char = '*'
                elif 23 <= column < 39:
                    char = '#'
                elif 39 <= column < 56:
                    char = '%'
                elif 56 <= column < 118:
                    char = '@'
                elif column == 118:
                    char = '%'
                elif column == 119:
                    char = '*'

            print(char, end='')
        print()

print_Gandhi_ji()
