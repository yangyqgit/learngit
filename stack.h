#pragma once
#include <queue>
#include <list>

template<class T>
class queue_stack
{
public:
	void push(const T& value)
	{
		if(!m_queue1.empty())
			m_queue1.push(value);
		else if(!m_queue2.empty())
			m_queue2.push(value);
		else
			m_queue1.push(value);
	}
	void pop()
	{
		if(!m_queue1.empty())
		{
			while(m_queue1.size() > 1)
			{
				m_queue2.push(m_queue1.front());
				m_queue1.pop();
			}
			m_queue1.pop();
		}
		else if(!m_queue2.empty())
		{
			while(m_queue2.size() > 1)
			{
				m_queue1.push(m_queue2.front());
				m_queue2.pop();
			}
			m_queue2.pop();
		}
	}
private:
	std::queue<T> m_queue1;
	std::queue<T> m_queue2;
};

template<class T>
class list_stack
{
public:
	void push(const T& value)
	{
		m_list.push_front(value);
	}
	void pop()
	{
		m_list.pop_front();
	}
private:
	std::list<T> m_list;
};