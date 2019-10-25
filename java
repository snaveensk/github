package web;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;


public class Junint_intro {

	@BeforeClass
	public static void setupbeforeclass() {
		System.out.println("before class");
	}
	@AfterClass
	public static void afterclass() {
		System.out.println("after class");
	}
	@Before
	public  void befor() {
		System.out.println("before method");
	}
	@After
	public  void after() {
		System.out.println("after method");
	}
	@Test
	public  void test1() {
		System.out.println("test_1");
	}
	@Test
	public  void test2() {
		System.out.println("test_2");
	}
}
