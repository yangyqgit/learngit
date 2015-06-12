#pragma once

struct lnode
{
	lnode*	m_next;
	int		m_value;
};


void insert_head(lnode** head, lnode* node)
{
	if(!head || node)
		return;
	if(0 == *head)
	{
		*head = node;
	}
	else
	{
		node->m_next = (*head)->m_next;
		(*head)->m_next = node;
	}
}

void insert_back(lnode** head, lnode* node)
{
	if(!head || node)
		return;
	if(0 == *head)
	{
		*head = node;
	}
	else
	{
		lnode* next = (*head)->m_next;
		while( next != 0 && next->m_next != 0)
			next = next->m_next;
		if(next != 0)
			next->m_next = node;
	}
}

void remove(lnode** head, lnode* node)
{
	if(!head || !*head || node)
		return;
	if(node->m_next)
	{
		node->m_value = node->m_next->m_value;
		node->m_next = node->m_next->m_next;
	}
	else
	{
		if(*head == node)
		{
			*head = 0;
		}
		else
		{
			lnode* next = (*head);
			while(next && next->m_next != node)
				next = next->m_next;
			if(next)
				next->m_next = 0;
		}
	}
}

#define recursive

lnode* reverse(lnode* head)
{
	if(!head || !head->m_next)
		return head;
#ifdef recursive
	else
	{
		lnode* new_head = reverse(head->m_next);
		// 对该节点及其后继节点进行反转
		head->m_next->m_next = head;
		head->m_next = 0;
		return new_head;
	}
#else
	lnode* new_head = head;
	lnode* next = head->m_next;
	head->m_next = 0;
	while(next)
	{
		lnode* current = next->m_next;
		next->m_next = new_head;
		new_head = next;
		next = current;
	}
	return new_head;
#endif
}

unsigned int length(lnode* head)
{
	if(!head)
		return 0;
	unsigned int len = 0;
	lnode* next = head;
	while(next)
	{
		++len;
		next = next->m_next;
	}
	return len;
}

lnode* rfind_k_node(lnode* head, int k)
{
	if(k == 0 || !head)
		return 0;
	lnode* ahead = head;
	lnode* behind = head;
	while(k > 1 && ahead != 0)
	{
		ahead = ahead->m_next;
		--k;
	}
	if(k > 1 || ahead == NULL)
		return 0;
	while(ahead->m_next)
	{
		ahead = ahead->m_next;
		behind = behind->m_next;
	}
	return behind;
}

lnode* find_middle_node(lnode* head)
{
	if(!head || !head->m_next)
		return head;
	lnode* ahead = head;
	lnode* behind = head;
	while(ahead->m_next)
	{
		ahead = ahead->m_next;
		behind = behind->m_next;
		if(ahead->m_next)
			ahead = ahead->m_next;
	}
	return behind;
}

void rprint(lnode* head)
{
	if(!head)
		return;
	else
	{
		print(head->m_next);
		printf("%d\n", head->m_value);
	}
}

lnode* merge_sorted_list(lnode* head1, lnode* head2)
{
	if(!head1)
		return head2;
	if(!head2)
		return head1;
	lnode* merged_head = 0;
#ifdef recursive
	if(head1->m_value < head2->m_value)
	{
		merged_head = head1;
		merged_head->m_next = merge_sorted_list(head1->m_next, head2);
	}
	else
	{
		merged_head = head2;
		merged_head->m_next = merge_sorted_list(head1, head2->m_next);
	}
#else
	if(head1->m_value < head2->m_value)
	{
		merged_head = head1;
		head1 = head1->m_next;
	}
	else
	{
		merged_head = head2;
		head2 = head2->m_next;
	}
	merged_head->m_next = 0;
	lnode* current = merged_head;
	while(head1 && head2)
	{
		if(head1->m_value < head2->m_value)
		{
			current->m_next = head1;
			head1 = head1->m_next;
		}
		else
		{
			current->m_next = head2;
			head2 = head2->m_next;
		}
		current = current->m_next;
		current->m_next = 0;
	}
	if(head1)
		current->m_next = head1;
	else if(head2)
		current->m_next = head2;
#endif
	return merged_head;
}

bool has_circle(lnode* head)
{
	if(!head)
		return false;
	lnode* fast = head;
	lnode* slow = head;
	while(fast->m_next)
	{
		fast = fast->m_next->m_next;
		slow = slow->m_next;
		if(slow == fast)
			return true;
	}
	return false;
}

bool test_intersect(lnode* head1, lnode* head2)
{
	if(!head1 || !head2)
		return false;
	lnode* tail1 = head1;
	while(tail1->m_next)
		tail1 = tail1->m_next;
	lnode* tail2 = head2;
	while(tail2->m_next)
		tail2 = tail2->m_next;
	return tail1 == tail2;
}

lnode* first_common_node(lnode* head1, lnode* head2)
{
	unsigned int len1 = length(head1);
	if(len1 == 0)
		return 0;
	unsigned int len2 = length(head2);
	if(len2 == 0)
		return 0;
	lnode* node1 = head1;
	lnode* node2 = head2;
	if(len1 > len2)
	{
		int k = len1 - len2;
		while(k --)
			node1 = node1->m_next;
	}
	else
	{
		int k = len2 - len1;
		while(k --)
			node2 = node2->m_next;
	}
	while(node1 && node2)
	{
		if(node1 == node2)
			return node1;
		node1 = node1->m_next;
		node2 = node2->m_next;
	}
	return 0;
}
