/**
 * 
 */
package com.sushank.hishob.dao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.sushank.hishob.model.User;
import com.sushank.hishob.util.HibernateUtil;

/**
 * @author sdahiwadkar
 *
 */
@Repository
public class UserDAOImpl implements UserDAO{
	
	@Autowired
	HibernateUtil hibernateUtil;
	
	public UserDAOImpl() {
		super();
		System.out.println("EmployeeDAOImpl constructor");
	}

	public long createUser(User user) {
		return (Long) hibernateUtil.create(user);
	}

	public User updateUser(User user) {
		return hibernateUtil.update(user);
	}

	public void deleteUser(long userId) {
		hibernateUtil.delete(userId);
	}

	public List<User> getAllUsers() {
		return hibernateUtil.fetchAll(User.class);
	}

	public User getUser(long userId) {
		return hibernateUtil.fetchById(userId, User.class);
	}

	public List<User> getAllUsers(String userName) {
		/*String query = "SELECT e.* FROM user e WHERE e.name like '%" + employeeName + "%'";
		List<Object[]> employeeObjects = hibernateUtil.fetchAll(query);
		List<Employee> employees = new ArrayList<Employee>();
		for (Object[] employeeObject : employeeObjects) {
			Employee employee = new Employee();
			long id = ((BigInteger) employeeObject[0]).longValue();
			int age = (int) employeeObject[1];
			String name = (String) employeeObject[2];
			float salary = (float) employeeObject[3];
			employee.setId(id);
			employee.setName(name);
			employee.setAge(age);
			employee.setSalary(salary);
			employees.add(employee);
		}
		System.out.println(employees);
		return employees;*/
		return null;
	}

}
