import os
from pathlib import Path

TOKEN_SETS = [
    {
        "fetch_token": "eyJhbGciOiJFUzI1NiIsIng1YyI6WyJNSUlFTVRDQ0E3YWdBd0lCQWdJUVI4S0h6ZG41NTRaL1VvcmFkTng5dHpBS0JnZ3Foa2pPUFFRREF6QjFNVVF3UWdZRFZRUURERHRCY0hCc1pTQlhiM0pzWkhkcFpHVWdSR1YyWld4dmNHVnlJRkpsYkdGMGFXOXVjeUJEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURUxNQWtHQTFVRUN3d0NSell4RXpBUkJnTlZCQW9NQ2tGd2NHeGxJRWx1WXk0eEN6QUpCZ05WQkFZVEFsVlRNQjRYRFRJMU1Ea3hPVEU1TkRRMU1Wb1hEVEkzTVRBeE16RTNORGN5TTFvd2daSXhRREErQmdOVkJBTU1OMUJ5YjJRZ1JVTkRJRTFoWXlCQmNIQWdVM1J2Y21VZ1lXNWtJR2xVZFc1bGN5QlRkRzl5WlNCU1pXTmxhWEIwSUZOcFoyNXBibWN4TERBcUJnTlZCQXNNSTBGd2NHeGxJRmR2Y214a2QybGtaU0JFWlhabGJHOXdaWElnVW1Wc1lYUnBiMjV6TVJNd0VRWURWUVFLREFwQmNIQnNaU0JKYm1NdU1Rc3dDUVlEVlFRR0V3SlZVekJaTUJNR0J5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEEwSUFCTm5WdmhjdjdpVCs3RXg1dEJNQmdyUXNwSHpJc1hSaTBZeGZlazdsdjh3RW1qL2JIaVd0TndKcWMyQm9IenNRaUVqUDdLRklJS2c0WTh5MC9ueW51QW1qZ2dJSU1JSUNCREFNQmdOVkhSTUJBZjhFQWpBQU1COEdBMVVkSXdRWU1CYUFGRDh2bENOUjAxREptaWc5N2JCODVjK2xrR0taTUhBR0NDc0dBUVVGQndFQkJHUXdZakF0QmdnckJnRUZCUWN3QW9ZaGFIUjBjRG92TDJObGNuUnpMbUZ3Y0d4bExtTnZiUzkzZDJSeVp6WXVaR1Z5TURFR0NDc0dBUVVGQnpBQmhpVm9kSFJ3T2k4dmIyTnpjQzVoY0hCc1pTNWpiMjB2YjJOemNEQXpMWGQzWkhKbk5qQXlNSUlCSGdZRFZSMGdCSUlCRlRDQ0FSRXdnZ0VOQmdvcWhraUc5Mk5rQlFZQk1JSCtNSUhEQmdnckJnRUZCUWNDQWpDQnRneUJzMUpsYkdsaGJtTmxJRzl1SUhSb2FYTWdZMlZ5ZEdsbWFXTmhkR1VnWW5rZ1lXNTVJSEJoY25SNUlHRnpjM1Z0WlhNZ1lXTmpaWEIwWVc1alpTQnZaaUIwYUdVZ2RHaGxiaUJoY0hCc2FXTmhZbXhsSUhOMFlXNWtZWEprSUhSbGNtMXpJR0Z1WkNCamIyNWthWFJwYjI1eklHOW1JSFZ6WlN3Z1kyVnlkR2xtYVdOaGRHVWdjRzlzYVdONUlHRnVaQ0JqWlhKMGFXWnBZMkYwYVc5dUlIQnlZV04wYVdObElITjBZWFJsYldWdWRITXVNRFlHQ0NzR0FRVUZCd0lCRmlwb2RIUndPaTh2ZDNkM0xtRndjR3hsTG1OdmJTOWpaWEowYVdacFkyRjBaV0YxZEdodmNtbDBlUzh3SFFZRFZSME9CQllFRklGaW9HNHdNTVZBMWt1OXpKbUdOUEFWbjNlcU1BNEdBMVVkRHdFQi93UUVBd0lIZ0RBUUJnb3Foa2lHOTJOa0Jnc0JCQUlGQURBS0JnZ3Foa2pPUFFRREF3TnBBREJtQWpFQStxWG5SRUM3aFhJV1ZMc0x4em5qUnBJelBmN1ZIejlWL0NUbTgrTEpsclFlcG5tY1B2R0xOY1g2WFBubGNnTEFBakVBNUlqTlpLZ2c1cFE3OWtuRjRJYlRYZEt2OHZ1dElETVhEbWpQVlQzZEd2RnRzR1J3WE95d1Iya1pDZFNyZmVvdCIsIk1JSURGakNDQXB5Z0F3SUJBZ0lVSXNHaFJ3cDBjMm52VTRZU3ljYWZQVGp6Yk5jd0NnWUlLb1pJemowRUF3TXdaekViTUJrR0ExVUVBd3dTUVhCd2JHVWdVbTl2ZENCRFFTQXRJRWN6TVNZd0pBWURWUVFMREIxQmNIQnNaU0JEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURVRNQkVHQTFVRUNnd0tRWEJ3YkdVZ1NXNWpMakVMTUFrR0ExVUVCaE1DVlZNd0hoY05NakV3TXpFM01qQXpOekV3V2hjTk16WXdNekU1TURBd01EQXdXakIxTVVRd1FnWURWUVFERER0QmNIQnNaU0JYYjNKc1pIZHBaR1VnUkdWMlpXeHZjR1Z5SUZKbGJHRjBhVzl1Y3lCRFpYSjBhV1pwWTJGMGFXOXVJRUYxZEdodmNtbDBlVEVMTUFrR0ExVUVDd3dDUnpZeEV6QVJCZ05WQkFvTUNrRndjR3hsSUVsdVl5NHhDekFKQmdOVkJBWVRBbFZUTUhZd0VBWUhLb1pJemowQ0FRWUZLNEVFQUNJRFlnQUVic1FLQzk0UHJsV21aWG5YZ3R4emRWSkw4VDBTR1luZ0RSR3BuZ24zTjZQVDhKTUViN0ZEaTRiQm1QaENuWjMvc3E2UEYvY0djS1hXc0w1dk90ZVJoeUo0NXgzQVNQN2NPQithYW85MGZjcHhTdi9FWkZibmlBYk5nWkdoSWhwSW80SDZNSUgzTUJJR0ExVWRFd0VCL3dRSU1BWUJBZjhDQVFBd0h3WURWUjBqQkJnd0ZvQVV1N0Rlb1ZnemlKcWtpcG5ldnIzcnI5ckxKS3N3UmdZSUt3WUJCUVVIQVFFRU9qQTRNRFlHQ0NzR0FRVUZCekFCaGlwb2RIUndPaTh2YjJOemNDNWhjSEJzWlM1amIyMHZiMk56Y0RBekxXRndjR3hsY205dmRHTmhaek13TndZRFZSMGZCREF3TGpBc29DcWdLSVltYUhSMGNEb3ZMMk55YkM1aGNIQnNaUzVqYjIwdllYQndiR1Z5YjI5MFkyRm5NeTVqY213d0hRWURWUjBPQkJZRUZEOHZsQ05SMDFESm1pZzk3YkI4NWMrbGtHS1pNQTRHQTFVZER3RUIvd1FFQXdJQkJqQVFCZ29xaGtpRzkyTmtCZ0lCQkFJRkFEQUtCZ2dxaGtqT1BRUURBd05vQURCbEFqQkFYaFNxNUl5S29nTUNQdHc0OTBCYUI2NzdDYUVHSlh1ZlFCL0VxWkdkNkNTamlDdE9udU1UYlhWWG14eGN4ZmtDTVFEVFNQeGFyWlh2TnJreFUzVGtVTUkzM3l6dkZWVlJUNHd4V0pDOTk0T3NkY1o0K1JHTnNZRHlSNWdtZHIwbkRHZz0iLCJNSUlDUXpDQ0FjbWdBd0lCQWdJSUxjWDhpTkxGUzVVd0NnWUlLb1pJemowRUF3TXdaekViTUJrR0ExVUVBd3dTUVhCd2JHVWdVbTl2ZENCRFFTQXRJRWN6TVNZd0pBWURWUVFMREIxQmNIQnNaU0JEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURVRNQkVHQTFVRUNnd0tRWEJ3YkdVZ1NXNWpMakVMTUFrR0ExVUVCaE1DVlZNd0hoY05NVFF3TkRNd01UZ3hPVEEyV2hjTk16a3dORE13TVRneE9UQTJXakJuTVJzd0dRWURWUVFEREJKQmNIQnNaU0JTYjI5MElFTkJJQzBnUnpNeEpqQWtCZ05WQkFzTUhVRndjR3hsSUVObGNuUnBabWxqWVhScGIyNGdRWFYwYUc5eWFYUjVNUk13RVFZRFZRUUtEQXBCY0hCc1pTQkpibU11TVFzd0NRWURWUVFHRXdKVlV6QjJNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQWlBMklBQkpqcEx6MUFjcVR0a3lKeWdSTWMzUkNWOGNXalRuSGNGQmJaRHVXbUJTcDNaSHRmVGpqVHV4eEV0WC8xSDdZeVlsM0o2WVJiVHpCUEVWb0EvVmhZREtYMUR5eE5CMGNUZGRxWGw1ZHZNVnp0SzUxN0lEdll1VlRaWHBta09sRUtNYU5DTUVBd0hRWURWUjBPQkJZRUZMdXczcUZZTTRpYXBJcVozcjY5NjYvYXl5U3JNQThHQTFVZEV3RUIvd1FGTUFNQkFmOHdEZ1lEVlIwUEFRSC9CQVFEQWdFR01Bb0dDQ3FHU000OUJBTURBMmdBTUdVQ01RQ0Q2Y0hFRmw0YVhUUVkyZTN2OUd3T0FFWkx1Tit5UmhIRkQvM21lb3locG12T3dnUFVuUFdUeG5TNGF0K3FJeFVDTUcxbWloREsxQTNVVDgyTlF6NjBpbU9sTTI3amJkb1h0MlFmeUZNbStZaGlkRGtMRjF2TFVhZ002QmdENTZLeUtBPT0iXX0.eyJ0cmFuc2FjdGlvbklkIjoiMzkwMDAyMjAxMjc2NjY0Iiwib3JpZ2luYWxUcmFuc2FjdGlvbklkIjoiMzkwMDAyMjAxMjc2NjY0Iiwid2ViT3JkZXJMaW5lSXRlbUlkIjoiMzkwMDAwOTkwODEyMjU4IiwiYnVuZGxlSWQiOiJjb20ubG9ja2V0LkxvY2tldCIsInByb2R1Y3RJZCI6ImxvY2tldF8xOTlfMW0iLCJzdWJzY3JpcHRpb25Hcm91cElkZW50aWZpZXIiOiIyMTQxOTQ0NyIsInB1cmNoYXNlRGF0ZSI6MTc3MTAxOTU3NDAwMCwib3JpZ2luYWxQdXJjaGFzZURhdGUiOjE3NzEwMTk1NzYwMDAsImV4cGlyZXNEYXRlIjoxNzczNDM1MTc0MDAwLCJxdWFudGl0eSI6MSwidHlwZSI6IkF1dG8tUmVuZXdhYmxlIFN1YnNjcmlwdGlvbiIsImRldmljZVZlcmlmaWNhdGlvbiI6IkZHelcyN0ovZjhXMFAwVU16emFSa0lMQk92VDUxV2d0RlRlaFlZUE9qeDhucU9CZm53QmZyS2FvZi9LQllaTUkiLCJkZXZpY2VWZXJpZmljYXRpb25Ob25jZSI6IjhlYjE1ZmRjLTMwOTMtNDhmOC1hZmQ3LTA4NWEwNDg1MTk0YSIsImluQXBwT3duZXJzaGlwVHlwZSI6IlBVUkNIQVNFRCIsInNpZ25lZERhdGUiOjE3NzEwMTk2MTI4MDgsImVudmlyb25tZW50IjoiUHJvZHVjdGlvbiIsInRyYW5zYWN0aW9uUmVhc29uIjoiUFVSQ0hBU0UiLCJzdG9yZWZyb250IjoiVk5NIiwic3RvcmVmcm9udElkIjoiMTQzNDcxIiwicHJpY2UiOjQ5MDAwMDAwLCJjdXJyZW5jeSI6IlZORCIsImFwcFRyYW5zYWN0aW9uSWQiOiI3MDUyODEyMzExNTYyMjYzOTcifQ.XwGDxjoQ9vpAfLynyCm9EctjmWRAbH0C8Sf93aHdrN-CAO9IoxHEkfOBAxoO1E28389yz6kHz2z9hZMwrA32_g",
        "app_transaction": "eyJhbGciOiJFUzI1NiIsIng1YyI6WyJNSUlFTVRDQ0E3YWdBd0lCQWdJUVI4S0h6ZG41NTRaL1VvcmFkTng5dHpBS0JnZ3Foa2pPUFFRREF6QjFNVVF3UWdZRFZRUURERHRCY0hCc1pTQlhiM0pzWkhkcFpHVWdSR1YyWld4dmNHVnlJRkpsYkdGMGFXOXVjeUJEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURUxNQWtHQTFVRUN3d0NSell4RXpBUkJnTlZCQW9NQ2tGd2NHeGxJRWx1WXk0eEN6QUpCZ05WQkFZVEFsVlRNQjRYRFRJMU1Ea3hPVEU1TkRRMU1Wb1hEVEkzTVRBeE16RTNORGN5TTFvd2daSXhRREErQmdOVkJBTU1OMUJ5YjJRZ1JVTkRJRTFoWXlCQmNIQWdVM1J2Y21VZ1lXNWtJR2xVZFc1bGN5QlRkRzl5WlNCU1pXTmxhWEIwSUZOcFoyNXBibWN4TERBcUJnTlZCQXNNSTBGd2NHeGxJRmR2Y214a2QybGtaU0JFWlhabGJHOXdaWElnVW1Wc1lYUnBiMjV6TVJNd0VRWURWUVFLREFwQmNIQnNaU0JKYm1NdU1Rc3dDUVlEVlFRR0V3SlZVekJaTUJNR0J5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEEwSUFCTm5WdmhjdjdpVCs3RXg1dEJNQmdyUXNwSHpJc1hSaTBZeGZlazdsdjh3RW1qL2JIaVd0TndKcWMyQm9IenNRaUVqUDdLRklJS2c0WTh5MC9ueW51QW1qZ2dJSU1JSUNCREFNQmdOVkhSTUJBZjhFQWpBQU1COEdBMVVkSXdRWU1CYUFGRDh2bENOUjAxREptaWc5N2JCODVjK2xrR0taTUhBR0NDc0dBUVVGQndFQkJHUXdZakF0QmdnckJnRUZCUWN3QW9ZaGFIUjBjRG92TDJObGNuUnpMbUZ3Y0d4bExtTnZiUzkzZDJSeVp6WXVaR1Z5TURFR0NDc0dBUVVGQnpBQmhpVm9kSFJ3T2k4dmIyTnpjQzVoY0hCc1pTNWpiMjB2YjJOemNEQXpMWGQzWkhKbk5qQXlNSUlCSGdZRFZSMGdCSUlCRlRDQ0FSRXdnZ0VOQmdvcWhraUc5Mk5rQlFZQk1JSCtNSUhEQmdnckJnRUZCUWNDQWpDQnRneUJzMUpsYkdsaGJtTmxJRzl1SUhSb2FYTWdZMlZ5ZEdsbWFXTmhkR1VnWW5rZ1lXNTVJSEJoY25SNUlHRnpjM1Z0WlhNZ1lXTmpaWEIwWVc1alpTQnZaaUIwYUdVZ2RHaGxiaUJoY0hCc2FXTmhZbXhsSUhOMFlXNWtZWEprSUhSbGNtMXpJR0Z1WkNCamIyNWthWFJwYjI1eklHOW1JSFZ6WlN3Z1kyVnlkR2xtYVdOaGRHVWdjRzlzYVdONUlHRnVaQ0JqWlhKMGFXWnBZMkYwYVc5dUlIQnlZV04wYVdObElITjBZWFJsYldWdWRITXVNRFlHQ0NzR0FRVUZCd0lCRmlwb2RIUndPaTh2ZDNkM0xtRndjR3hsTG1OdmJTOWpaWEowYVdacFkyRjBaV0YxZEdodmNtbDBlUzh3SFFZRFZSME9CQllFRklGaW9HNHdNTVZBMWt1OXpKbUdOUEFWbjNlcU1BNEdBMVVkRHdFQi93UUVBd0lIZ0RBUUJnb3Foa2lHOTJOa0Jnc0JCQUlGQURBS0JnZ3Foa2pPUFFRREF3TnBBREJtQWpFQStxWG5SRUM3aFhJV1ZMc0x4em5qUnBJelBmN1ZIejlWL0NUbTgrTEpsclFlcG5tY1B2R0xOY1g2WFBubGNnTEFBakVBNUlqTlpLZ2c1cFE3OWtuRjRJYlRYZEt2OHZ1dElETVhEbWpQVlQzZEd2RnRzR1J3WE95d1Iya1pDZFNyZmVvdCIsIk1JSURGakNDQXB5Z0F3SUJBZ0lVSXNHaFJ3cDBjMm52VTRZU3ljYWZQVGp6Yk5jd0NnWUlLb1pJemowRUF3TXdaekViTUJrR0ExVUVBd3dTUVhCd2JHVWdVbTl2ZENCRFFTQXRJRWN6TVNZd0pBWURWUVFMREIxQmNIQnNaU0JEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURVRNQkVHQTFVRUNnd0tRWEJ3YkdVZ1NXNWpMakVMTUFrR0ExVUVCaE1DVlZNd0hoY05NakV3TXpFM01qQXpOekV3V2hjTk16WXdNekU1TURBd01EQXdXakIxTVVRd1FnWURWUVFERER0QmNIQnNaU0JYYjNKc1pIZHBaR1VnUkdWMlpXeHZjR1Z5SUZKbGJHRjBhVzl1Y3lCRFpYSjBhV1pwWTJGMGFXOXVJRUYxZEdodmNtbDBlVEVMTUFrR0ExVUVDd3dDUnpZeEV6QVJCZ05WQkFvTUNrRndjR3hsSUVsdVl5NHhDekFKQmdOVkJBWVRBbFZUTUhZd0VBWUhLb1pJemowQ0FRWUZLNEVFQUNJRFlnQUVic1FLQzk0UHJsV21aWG5YZ3R4emRWSkw4VDBTR1luZ0RSR3BuZ24zTjZQVDhKTUViN0ZEaTRiQm1QaENuWjMvc3E2UEYvY0djS1hXc0w1dk90ZVJoeUo0NXgzQVNQN2NPQithYW85MGZjcHhTdi9FWkZibmlBYk5nWkdoSWhwSW80SDZNSUgzTUJJR0ExVWRFd0VCL3dRSU1BWUJBZjhDQVFBd0h3WURWUjBqQkJnd0ZvQVV1N0Rlb1ZnemlKcWtpcG5ldnIzcnI5ckxKS3N3UmdZSUt3WUJCUVVIQVFFRU9qQTRNRFlHQ0NzR0FRVUZCekFCaGlwb2RIUndPaTh2YjJOemNDNWhjSEJzWlM1amIyMHZiMk56Y0RBekxXRndjR3hsY205dmRHTmhaek13TndZRFZSMGZCREF3TGpBc29DcWdLSVltYUhSMGNEb3ZMMk55YkM1aGNIQnNaUzVqYjIwdllYQndiR1Z5YjI5MFkyRm5NeTVqY213d0hRWURWUjBPQkJZRUZEOHZsQ05SMDFESm1pZzk3YkI4NWMrbGtHS1pNQTRHQTFVZER3RUIvd1FFQXdJQkJqQVFCZ29xaGtpRzkyTmtCZ0lCQkFJRkFEQUtCZ2dxaGtqT1BRUURBd05vQURCbEFqQkFYaFNxNUl5S29nTUNQdHc0OTBCYUI2NzdDYUVHSlh1ZlFCL0VxWkdkNkNTamlDdE9udU1UYlhWWG14eGN4ZmtDTVFEVFNQeGFyWlh2TnJreFUzVGtVTUkzM3l6dkZWVlJUNHd4V0pDOTk0T3NkY1o0K1JHTnNZRHlSNWdtZHIwbkRHZz0iLCJNSUlDUXpDQ0FjbWdBd0lCQWdJSUxjWDhpTkxGUzVVd0NnWUlLb1pJemowRUF3TXdaekViTUJrR0ExVUVBd3dTUVhCd2JHVWdVbTl2ZENCRFFTQXRJRWN6TVNZd0pBWURWUVFMREIxQmNIQnNaU0JEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURVRNQkVHQTFVRUNnd0tRWEJ3YkdVZ1NXNWpMakVMTUFrR0ExVUVCaE1DVlZNd0hoY05NVFF3TkRNd01UZ3hPVEEyV2hjTk16a3dORE13TVRneE9UQTJXakJuTVJzd0dRWURWUVFEREJKQmNIQnNaU0JTYjI5MElFTkJJQzBnUnpNeEpqQWtCZ05WQkFzTUhVRndjR3hsSUVObGNuUnBabWxqWVhScGIyNGdRWFYwYUc5eWFYUjVNUk13RVFZRFZRUUtEQXBCY0hCc1pTQkpibU11TVFzd0NRWURWUVFHRXdKVlV6QjJNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQWlBMklBQkpqcEx6MUFjcVR0a3lKeWdSTWMzUkNWOGNXalRuSGNGQmJaRHVXbUJTcDNaSHRmVGpqVHV4eEV0WC8xSDdZeVlsM0o2WVJiVHpCUEVWb0EvVmhZREtYMUR5eE5CMGNUZGRxWGw1ZHZNVnp0SzUxN0lEdll1VlRaWHBta09sRUtNYU5DTUVBd0hRWURWUjBPQkJZRUZMdXczcUZZTTRpYXBJcVozcjY5NjYvYXl5U3JNQThHQTFVZEV3RUIvd1FGTUFNQkFmOHdEZ1lEVlIwUEFRSC9CQVFEQWdFR01Bb0dDQ3FHU000OUJBTURBMmdBTUdVQ01RQ0Q2Y0hFRmw0YVhUUVkyZTN2OUd3T0FFWkx1Tit5UmhIRkQvM21lb3locG12T3dnUFVuUFdUeG5TNGF0K3FJeFVDTUcxbWloREsxQTNVVDgyTlF6NjBpbU9sTTI3amJkb1h0MlFmeUZNbStZaGlkRGtMRjF2TFVhZ002QmdENTZLeUtBPT0iXX0.eyJyZWNlaXB0VHlwZSI6IlByb2R1Y3Rpb24iLCJhcHBBcHBsZUlkIjoxNjAwNTI1MDYxLCJidW5kbGVJZCI6ImNvbS5sb2NrZXQuTG9ja2V0IiwiYXBwbGljYXRpb25WZXJzaW9uIjoiMyIsInZlcnNpb25FeHRlcm5hbElkZW50aWZpZXIiOjg4MjMyMDkxNiwicmVjZWlwdENyZWF0aW9uRGF0ZSI6MTc3MDk5MzQxNzQzMiwicmVxdWVzdERhdGUiOjE3NzA5OTM0MTc0MzIsIm9yaWdpbmFsUHVyY2hhc2VEYXRlIjoxNjcxNDU1MTU5MDEzLCJvcmlnaW5hbEFwcGxpY2F0aW9uVmVyc2lvbiI6IjciLCJkZXZpY2VWZXJpZmljYXRpb24iOiJwZTNxZXV1eDZVUDZmekI0b3p0REc3NSsrZ1hYODBONldFY0IyOUozWk0vN3d6ZzhyQUNCQnZYV29UZWFBNmFzIiwiZGV2aWNlVmVyaWZpY2F0aW9uTm9uY2UiOiJhZTE2ZDg0MC1hODIzLTRlMzYtYWVjZC0wMGVlZmU0ZDZhZTciLCJhcHBUcmFuc2FjdGlvbklkIjoiNzA1MjgxMjMxMTU2MjI2Mzk3Iiwib3JpZ2luYWxQbGF0Zm9ybSI6ImlPUyJ9.hSQFy0GNK1bJDeUEfL1fg_RDnPFnCUawfbmQUVbS8EdOhQ6_anISSNQH7-V0xoJd5lnu8vQXf5FvDmX8xb0iDQ",
        "x-post-params-hash": "app_user_id,fetch_token,app_transaction:sha256:41cbb77ad46c902e219af52e9432e26b4bf88720c3622c2118c56e33ca798061",
        "x-headers-hash": "X-Is-Sandbox:sha256:fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa",
        "is_sandbox": True,
    }
]

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    with ENV_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
NEXTDNS_KEY = os.environ.get("NEXTDNS_KEY")

ADMIN_ID = 5645750335
NUM_WORKERS = 1
DONATE_PHOTO = "AgACAgUAAxkBAAEhBOdpjtu4_D_90mzmM3ax-jLUQbW7HwACjA5rGyK6eFQz2Vzy6zHTMwEAAwIAA3kAAzoE"

E_LOADING = '<tg-emoji emoji-id="5350752364246606166">✍️</tg-emoji>'
E_LIMIT   = '<tg-emoji emoji-id="5424857974784925603">🚫</tg-emoji>'
E_SUCCESS = '<tg-emoji emoji-id="5260463209562776385">✅</tg-emoji>'
E_ERROR   = '<tg-emoji emoji-id="5318840353510408444">🔴</tg-emoji>'
E_TIP     = '<tg-emoji emoji-id="4968003407315993509">💡</tg-emoji>'
E_MENU    = '<tg-emoji emoji-id="5449601904147440135">👑</tg-emoji>'

E_USER    = '<tg-emoji emoji-id="5974048815789903111">👤</tg-emoji>'
E_ID      = '<tg-emoji emoji-id="5974526806995242353">🆔</tg-emoji>'
E_TAG     = '<tg-emoji emoji-id="5240228673738527951">🏷️</tg-emoji>'
E_STAT    = '<tg-emoji emoji-id="4967519884192777037">📊</tg-emoji>'
E_GLOBE   = '<tg-emoji emoji-id="5231489647946768652">🌐</tg-emoji>'
E_SOS     = '<tg-emoji emoji-id="6301027265899661025">🆘</tg-emoji>'
E_SHIELD  = '<tg-emoji emoji-id="5352888345972187597">🛡️</tg-emoji>'
E_CALENDAR = '<tg-emoji emoji-id="5413879192267805083">📅</tg-emoji>'
E_IOS     = '<tg-emoji emoji-id="5350556204500263431">🍏</tg-emoji>'
E_ANDROID = '<tg-emoji emoji-id="5303145396254563405">🤖</tg-emoji>'


DEFAULT_LANG = "VI"

TEXTS = {
    "VI": {
        "welcome": (
            f"{E_SUCCESS} <b>Locket Gold Activator</b>\n\n"
            f"Chào mừng bạn đến với hệ thống kích hoạt Locket Gold tự động.\n"
            f"Vui lòng chọn ngôn ngữ hoặc sử dụng các nút bên dưới để bắt đầu.\n"
            f"Liên hệ <b>Admin</b>: @sweep207."
        ),
        "menu_msg": (
            f"{E_MENU} <b>Bảng điều khiển chính</b>\n\n"
            f"👇 Nhấn nút bên dưới để nhập Username Locket cần kích hoạt Gold."
        ),
        "btn_input": "🔑 Nhập Username Locket",
        "btn_lang": "🌐 Đổi Ngôn Ngữ",
        "btn_help": "🆘 Hỗ Trợ",
        "prompt_input": (
            f"{E_LOADING} Vui lòng trả lời tin nhắn này bằng <b>Username</b> "
            f"hoặc <b>Link Locket</b> chính xác của bạn để hệ thống xử lý."
        ),
        "lang_select": "🌐 Vui lòng chọn ngôn ngữ hiển thị / Please select language:",
        "lang_set": f"{E_SUCCESS} Ngôn ngữ đã được đặt thành: Tiếng Việt",
        "help_msg": (
            f"<b>{E_MENU} Danh sách lệnh:</b>\n\n"
            f"/start - Khởi động bot và mở menu chính\n"
            f"/setlang - Thay đổi ngôn ngữ (VI/EN)\n"
            f"/help - Xem hướng dẫn chi tiết\n\n"
            f"<b>{E_TIP} Hướng dẫn sử dụng nhanh:</b>\n"
            f"1. Nhấn nút '🔑 Nhập Username Locket'\n"
            f"2. Nhập Username hoặc đường dẫn Locket chính xác\n"
            f"3. Hệ thống sẽ kiểm tra trạng thái và hỗ trợ kích hoạt Gold (nếu đủ điều kiện)."
        ),
        "resolving": f"{E_LOADING} <b>Đang phân tích và lấy thông tin tài khoản...</b>",
        "not_found": f"{E_ERROR} Không tìm thấy User.",
        "limit_reached": f"{E_LIMIT} Bạn đã đạt đến giới hạn số lần sử dụng trong ngày (5/5). Vui lòng quay lại sau.",
        "queue_almost": (
            f"{E_LOADING} <b>Sắp đến lượt xử lý yêu cầu của bạn.</b>\n"
            f"Còn <b>2 người</b> nữa trong hàng chờ. Vui lòng chờ trong giây lát."
        ),
        "admin_noti_sent": f"{E_SUCCESS} Đã gửi thông báo đến toàn bộ người dùng trong hệ thống.",
        "admin_reset": f"{E_SUCCESS} Đã đặt lại lượt sử dụng cho người dùng {{}}.",
        "admin_only": f"{E_ERROR} Bạn không có quyền sử dụng lệnh này.",
        "checking_status": f"{E_LOADING} <b>Đang kiểm tra trạng thái gói Gold...</b>",
        "free_status": "Free (chưa kích hoạt)",
        "gold_active": f"{E_SUCCESS} <b>Gold đang hoạt động</b> (Hết hạn: {{}})",
        "user_info_title": f"{E_USER} <b>User Information</b>",
        "btn_upgrade": "🚀 KÍCH HOẠT NGAY",
        "queued": (
            f"{E_LOADING} <b>Yêu cầu của bạn đã được đưa vào hàng chờ xử lý.</b>\n"
            f"Tài khoản: <code>{{0}}</code>\n"
            f"Vị trí hiện tại: <b>#{{1}}</b> (Còn {{2}} yêu cầu phía trước)."
        ),
        "processing": (
            f"{E_LOADING} <b>Hệ thống đang xử lý yêu cầu kích hoạt Gold...</b>\n"
            f"<pre>"
            f"[*] Tài khoản: {{}}\n"
            f"[*] Đang gửi yêu cầu tới máy chủ dịch vụ\n"
            f"[>] Đang chờ phản hồi xác nhận\n"
            f"[>] Vui lòng không thao tác thêm cho đến khi hoàn tất"
            f"</pre>"
        ),
        "success_title": f"{E_SUCCESS} <b>KÍCH HOẠT THÀNH CÔNG GÓI GOLD</b>",
        "generating_dns": f"{E_SHIELD} Đang tạo cấu hình DNS chống thu hồi (Anti-Revoke)...",
        "fail_title": f"{E_ERROR} <b>Kích hoạt không thành công</b>",
        "dns_msg": (
            f"{E_SHIELD} <b>HƯỚNG DẪN QUAN TRỌNG SAU KHI KÍCH HOẠT</b>:\n"
            f"1️⃣ Mở ứng dụng Locket và kiểm tra trạng thái <b>Gold</b> của tài khoản.\n"
            f"2️⃣ Nếu đã thấy Gold, vui lòng <b>cài đặt DNS bảo vệ ngay</b> trong vòng 45 giây:\n\n"
            f"{E_IOS} <b>Người dùng iOS</b>: <a href='{{}}'>Nhấn vào đây để cài đặt</a>\n"
            f"(Mở liên kết bằng <b>Safari</b> → Cho phép → Cài đặt cấu hình cấu hình mạng).\n\n"
            f"{E_ANDROID} <b>Người dùng Android</b>: sử dụng cấu hình DNS: <code>{{}}.dns.nextdns.io</code>\n"
            f"(Cài đặt → Mạng & Internet → DNS riêng tư / Private DNS).\n\n"
            f"{E_TIP} <b>Lưu ý</b>: Việc cài đặt DNS là bắt buộc để hạn chế nguy cơ mất Gold trong tương lai."
        )
    },
    "EN": {
        "welcome": (
            f"{E_SUCCESS} <b>Locket Gold Activator</b>\n\n"
            f"Welcome to the automated Locket Gold activation assistant.\n"
            f"Please select your preferred language or use the menu below to get started.\n"
            f"Contacs <b>Admin</b>: @sweep207."
        ),
        "menu_msg": (
            f"{E_MENU} <b>Main Control Panel</b>\n\n"
            f"👇 Click the button below to provide the Locket Username you want to activate."
        ),
        "btn_input": "🔑 Enter Locket Username",
        "btn_lang": "🌐 Change Language",
        "btn_help": "🆘 Help",
        "prompt_input": (
            f"{E_LOADING} Please reply to this message with your exact <b>Username</b> "
            f"or <b>Locket Link</b> so the system can process your request."
        ),
        "lang_select": "🌐 Please select your display language:",
        "lang_set": f"{E_SUCCESS} Language has been set to English.",
        "help_msg": (
            f"<b>{E_MENU} Available commands:</b>\n\n"
            f"/start - Start the bot and open the main menu\n"
            f"/setlang - Change language (VI/EN)\n"
            f"/help - Show detailed usage guide\n\n"
            f"<b>{E_TIP} Quick usage guide:</b>\n"
            f"1. Click '🔑 Enter Locket Username'\n"
            f"2. Enter the correct Username or Locket link\n"
            f"3. The system will check your status and assist with Gold activation when eligible."
        ),
        "resolving": f"{E_LOADING} <b>Analyzing and retrieving account information...</b>",
        "not_found": f"{E_ERROR} User not found.",
        "limit_reached": f"{E_LIMIT} You have reached the daily usage limit (5/5). Please try again tomorrow.",
        "queue_almost": (
            f"{E_LOADING} <b>Your request is almost being processed.</b>\n"
            f"There are <b>2 requests</b> ahead of you. Please wait a moment."
        ),
        "admin_noti_sent": f"{E_SUCCESS} Notification has been sent to all registered users.",
        "admin_reset": f"{E_SUCCESS} Daily usage has been reset for user {{}}.",
        "admin_only": f"{E_ERROR} You don't have permission.",
        "checking_status": f"{E_LOADING} <b>Checking current Gold entitlement status...</b>",
        "free_status": "Free (not activated)",
        "gold_active": f"{E_SUCCESS} <b>Gold is currently active</b> (Expiry: {{}})",
        "user_info_title": f"{E_USER} <b>User Information</b>",
        "btn_upgrade": "🚀 ACTIVATE NOW",
        "queued": (
            f"{E_LOADING} <b>Your request has been added to the processing queue.</b>\n"
            f"Target account: <code>{{0}}</code>\n"
            f"Current position: <b>#{{1}}</b> ({{2}} requests ahead of you)."
        ),
        "processing": (
            f"{E_LOADING} <b>The system is processing your Gold activation request...</b>\n"
            f"<pre>"
            f"[*] Account: {{}}\n"
            f"[*] Sending request to the service backend\n"
            f"[>] Awaiting confirmation from the server\n"
            f"[>] Please avoid additional actions until the process is complete"
            f"</pre>"
        ),
        "success_title": f"{E_SUCCESS} <b>GOLD ACTIVATION SUCCESSFUL</b>",
        "generating_dns": f"{E_SHIELD} Generating Anti-Revoke DNS configuration...",
        "fail_title": f"{E_ERROR} <b>Activation was not successful</b>",
        "dns_msg": (
            f"{E_SHIELD} <b>IMPORTANT STEPS AFTER ACTIVATION</b>:\n"
            f"1️⃣ Open the Locket app and verify that your account shows <b>Gold</b> status.\n"
            f"2️⃣ If Gold is active, please <b>install the DNS configuration immediately</b> within 45 seconds:\n\n"
            f"{E_IOS} <b>For iOS users</b>: <a href='{{}}'>Click here to install</a>\n"
            f"(Open the link in <b>Safari</b> → Allow → Install the network configuration profile).\n\n"
            f"{E_ANDROID} <b>For Android users</b>: use the following DNS configuration: <code>{{}}.dns.nextdns.io</code>\n"
            f"(Settings → Network & Internet → Private DNS).\n\n"
            f"{E_TIP} <b>Note</b>: Installing DNS is required to reduce the risk of losing Gold in the future."
        )
    }
}

def T(key, lang=None):
    if not lang:
        lang = DEFAULT_LANG
    return TEXTS.get(lang, TEXTS["VI"]).get(key, key)