/**
 * 
 */
package com.sushank.hishob.service;

import java.util.List;

import com.sushank.hishob.model.User;

/**
 * @author sdahiwadkar
 *
 */
public interface UserService {
	public long createUser(User user);
	
    public User updateUser(User user);
    
    public void deleteUser(long id);
    
    public List<User> getAllUsers();
    
    public User getUser(long id);
    
    public List<User> getAllUsers(String userName);
}
