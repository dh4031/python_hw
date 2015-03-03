import pexpect
import os
import glob

os.chdir("/home/vagrant/examples") #where my primates file lives

def mbRunner(fname, ngen = 5000):
    #this function starts a mrbayes run with fname for ngen generations
    child = pexpect.spawn("mb -i {}".format(fname))
    child.sendline(r"set nowarn = yes")
    child.expect("MrBayes >")
    child.sendline(r"mcmcp ngen = {}".format(ngen))
    child.expect("MrBayes >")
    child.sendline(r"mcmc")
    child.sendline(r"no")
    child.expect("MrBayes >")
    child.sendline(r"quit")

def sumRunner(fname):
	#this function uses mrbayes to run sump and sumt
	child = pexpect.spawn("mb -i")
	child.sendline(r"execute {}".format(fname))
	child.expect("MrBayes >")
	child.sendline(r"set nowarn = yes")
	child.expect("MrBayes >")
	child.sendline(r"sumt")
	child.expect("MrBayes >")
	child.sendline(r"sump")
	child.expect("MrBayes >")
	child.sendline(r"quit")

beforeFF = glob.glob("*.*")
beforeTreeFF = glob.glob("*.t")

runFF = "primtates2.nex"

print "Before there were {} files in the directory and {} than end in '.t'".format(len(beforeFF), len(beforeTreeFF))


mbRunner(runFF, 6000)
sumRunner(runFF)

afterFF = glob.glob("*.*")
print "Now there are {} files in the directory and {} than end in '.t'".format(len(afterFF), len(glob.glob("*.t")))
afterTree = glob.glob("*.t")
print "The tree files are: " + ", ".join(afterTree) + "."