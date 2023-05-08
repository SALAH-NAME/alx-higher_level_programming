#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the head node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *end = list;

	while(end != NULL)
	{
		if(list == end->next)
			return (1);
		end = end->next;
	}

	return (0);
}
