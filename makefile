FILES :=                              \
    .travis.yml                       \
    .gitignore                        \
    FizzBuzz.py                       \
    RunFizzBuzzDefault.py             \
    RunFizzBuzzDefault.out            \
    RunFizzBuzzCustom.py              \
    RunFizzBuzzCustom.in              \
    RunFizzBuzzCustom.out             \
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
	rm -rf __pycache__
	rm -f  TestFizzBuzz.tmp
	rm -f  RunFizzBuzzDefault.tmp
	rm -f  RunFizzBuzzCustom.tmp

config:
	git config -l

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: RunFizzBuzzDefault.tmp RunFizzBuzzCustom.tmp TestFizzBuzz.tmp

TestFizzBuzz.tmp: TestFizzBuzz.py
	coverage3 run    --branch TestFizzBuzz.py >  TestFizzBuzz.tmp 2>&1
	coverage3 report -m                      >> TestFizzBuzz.tmp
	cat TestFizzBuzz.tmp

RunFizzBuzzDefault.tmp: RunFizzBuzzDefault.out RunFizzBuzzDefault.py
	chmod +x RunFizzBuzzDefault.py
	./RunFizzBuzzDefault.py > RunFizzBuzzDefault.tmp
	diff RunFizzBuzzDefault.tmp RunFizzBuzzDefault.out

RunFizzBuzzCustom.tmp: RunFizzBuzzCustom.in RunFizzBuzzCustom.out RunFizzBuzzCustom.py
	chmod +x RunFizzBuzzCustom.py
	./RunFizzBuzzCustom.py < RunFizzBuzzCustom.in > RunFizzBuzzCustom.tmp
	diff RunFizzBuzzCustom.tmp RunFizzBuzzCustom.out

fb_default: RunFizzBuzzDefault.py
	chmod +x RunFizzBuzzDefault.py
	./RunFizzBuzzDefault.py

fb_custom: RunFizzBuzzCustom.py
	chmod +x RunFizzBuzzCustom.py
	./RunFizzBuzzCustom.py < RunFizzBuzzCustom.in
