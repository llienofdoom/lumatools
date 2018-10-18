import sys, os, glob

args     = sys.argv[1:]
folder   = os.path.dirname(args[0])
filename = os.path.basename(args[0])
name     = filename.split('.')[0]
number   = filename.split('.')[1]
ext      = filename.split('.')[2]

list_of_files = glob.glob(folder + os.sep + name + '.????.' + ext)
first = int(os.path.basename(list_of_files[0]).split('.')[1])

print '#'*80
print 'Found %d files matching pattern in %s.' % (len(list_of_files), folder)
print 'Pattern is [name].[number].[ext]. Thus %s.####.%s.' % (name, ext)
print 'This will NOT work if this is not the convention. So there...'
print
print 'What do you want to change? [1].[2].[3] : ',
choice = int(raw_input())
if choice == 1:
    print 'You chose wrong! Only kidding, you chose changing the name.'
    print 'Please enter new name : ',
    name = raw_input()
if choice == 2:
    print 'Whooa! Look at you. Changing the number like you don\'t care.'
    print 'Currently starting from %d.' % first
    print 'Please enter new starting frame number : ',
    first = int(raw_input())
if choice == 3:
    print 'You\'re kidding, right? This is not the tool for converting files.'
    print 'Go jump off a bridge.'
    raw_input()
    exit(0)
print 'Thanks. You\'re awesome.'
print 'So, the sequence will be renamed'
print 'From  : %s.####.%s' % (filename.split('.')[0], ext)
print 'To    : %s.%04d.%s' % (name, first, ext)
print 'Is this correct? [y/n] : ',
correct = raw_input()
if correct == 'y':
    for i in list_of_files:
        print 'Renaming %s' % i
        newnumber = '%04d' % first
        newname   = folder + os.sep + name + '.' + newnumber + '.' + ext
        print 'To %s' % newname,
        os.rename(i, newname)
        first = first + 1
        print 'Done!'

print
print 'Nice. Well done. Have a great day.'
raw_input()
