#include "lists.h"
/**
 * check_cycle - function that verify if is cycle
 * @list: parameter of entry it is list to verify
 * Return: 0 if is empty or 1 if is value diferent 0
**/
int check_cycle(listint_t *list)
{
	listint_t *object_tur = list;
	listint_t *object_har = list;

	object_har = list;
	object_tur = list->next;

	if (list == NULL)
	{
		return (0);
		while (object_har != NULL && object_har->next != NULL)
		{
			if (object_tur == object_har)
			{
				return (1);
			}
		}
	}
	return (0);
}
