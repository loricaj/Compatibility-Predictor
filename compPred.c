/*
 *	Joshua Lorica
 *	4/5/2022
 *	DataHouse Coding Assignment
 *	Compatability Predictor
 */

#include<stdio.h>
#include<json-c/json.h>	//json library

int main(int argc, char **argv){
	//file pointer	
	FILE *fp;
	//character buffer
	char buffer[1024];

	//initialize structures	
	struct json_object *parsed_json;
	struct json_object *parsed_json_array;
	struct json_object *name;
	struct json_object *attributes;
	struct json_object *intelligence;
	struct json_object *strength;
	struct json_object *endurance;
	struct json_object *spicyFoodTolerance;

	//open and read file (data.json)
	fp = fopen("data.json", "r");
	fread(buffer, 1024, 1, fp);
	fclose(fp);

	//parse json strings
	parsed_json = json_tokener_parse(buffer);

	//access array in json file
	//DOES NOT WORK
	parsed_json_array = json_object_object_get_ex(parsed_json, "team[0].attributes", &attributes);

	//get name from json file
	json_object_object_get_ex(parsed_json, "name" , &name);

	//print name
	//TODO: change output to JSON
	printf("Name: %s\n", json_object_get_string(name));

	/*
	Algorithim to solve for Compatability:
	Average each team member's attributes
	Average each team member's attribute average
	Average each applicant's attributes
	Compare each applicant's attribute average to the team members attribute average
	Absolute value of difference
      	Divide by 10 to get in [0,1] range	
	Output to JSON
	*/
}
