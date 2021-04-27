#include "lists.h"
/**
 * check_cycle - function that verify if is cycle
 * @list: parameter of entry it is list to verify
 * Return: 0 if is empty or 1 if is value diferent 0
**/
int check_cycle(listint_t *list)
{
	listint_t object1 = list;
	listint_t object2 = list;

	object2 = list;
	object1 = list->next;

	if (list == '\0' || list->next == '\0' || object1->next == '\0')
	{
		return (0);
	}

	while (object1 != '\0')
	{
		if (object1 == object2)
		{
			return (1);
		}
	}
	return (0);
}
