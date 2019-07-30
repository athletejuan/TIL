# python 가상환경 만들기 (python 3.7.4 --> 3.5.3)



#### gitbash 에서

mkdir ~/python-virtualenv

python -m venv ~/python-virtualenv/3.7.4

cd codes

mkdir django

cd django

source ~/python-virtualenv/3.7.4/Scripts/activate

exit: deactivate



cd ~

code .

.bashrc

(alias venv='source ~/python-virtualenv/3.7.4/Scripts/activate')

source ~/.bashrc

venv 