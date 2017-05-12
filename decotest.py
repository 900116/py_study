#encoding=utf-8
interface myInterface()
func1()
func2()

class A implement  myInterface
	myInterface instance;
	public A(myInterface x)
	{
		this.instance = x
	}

	public void func1()
	{
	    this.instance.func1()
	    //other smth
	}



class B implement  myInterface
	myInterface instance;
	public B(myInterface x)
	{
		this.instance = x
	}

	public void func1()
	{
	    this.instance.func1()
	    //other smth
	}
