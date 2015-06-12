#pragma once
#include <stack>
#include <list>

template<class T>
class stack_queue
{
	void push(const T& value)
	{
		m_stack1.push(value);
	}
	void pop()
	{
		if(m_stack2.empty())
		{
			while(!m_stack1.empty())
			{
				m_stack2.push(m_stack1.top());
				m_stack1.pop();
			}
		}
		m_stack2.pop();
	}
private:
	std::stack<T> m_stack1;
	std::stack<T> m_stack2;
};

template<class T>
class list_queue
{
public:
	void push(const T& value)
	{
		m_list.push_back(value);
	}
	void pop()
	{
		m_list.pop_front();
	}
private:
	std::list<T> m_list;
};