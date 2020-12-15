import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import java.io.IOException;
import java.io.InputStream;

/**
 * Created By fct on 2020/12/14
 * Using SoftWare  :   IntelliJ IDEA
 * ProjectName     :   demo01
 */
public class MyTest {

	String resource = "src/main/resources/mybatis-config.xml";
	InputStream inputStream = Resources.getResourceAsStream(resource);
	SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);

	public MyTest() throws IOException {
	}
}
