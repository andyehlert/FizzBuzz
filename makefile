FILES :=                              \
    .travis.yml                       \
    .gitignore                        \
    FizzBuzz.py                       \
    TestFizzBuzz.py

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	# rm -f  *.pyc
	rm -rf __pycache__
	rm -f  TestFizzBuzz.tmp

config:
	git config -l

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: TestFizzBuzz.py
	coverage3 run    --branch TestFizzBuzz.py >  TestFizzBuzz.tmp 2>&1
	coverage3 report -m                      >> TestFizzBuzz.tmp
	cat TestFizzBuzz.tmp