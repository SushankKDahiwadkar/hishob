/**
 * 
 */
package com.sushank.hishob.dao;

import java.util.List;

import com.sushank.hishob.model.User;

/**
 * @author sdahiwadkar
 *
 */
public interface UserDAO {
	public long createUser(User user);
	
    public User updateUser(User user);
    
    public void deleteUser(long id);
    
    public List<User> getAllUsers();
    
    public User getUser(long id);
    
    public List<User> getAllUsers(String userName);
}
