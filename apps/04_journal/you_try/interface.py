import program


def main():
    header()
    action()


def header():
    print('------------------------------')
    print('     Personal Journal App')
    print('------------------------------')
    print()

def action():
    cmd = 'EMPTY'
    journal_name = 'default'
    existing_entries = program.load(journal_name)  # []  # list()
    print()
    print('What do you want to do with your journal?')

    while cmd != 'x' and cmd:
        print('[L]ist, [A]dd, or E[x]it? ')
        cmd = input().lower().strip()
        if cmd == 'l':
            list_entries(existing_entries)
        elif cmd == 'a':
            add_entry(existing_entries)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    program.save(journal_name, existing_entries)

def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    program.add_entry(text, data)


if __name__ == '__main__':
    main()

