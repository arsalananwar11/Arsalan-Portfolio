class GeneralHelper():
    def get_experience_row_index(self, experience_list):
        row_index_list = [1]
        for i in range(1, len(experience_list)):
            current_org = experience_list[i][2]
            previous_org = experience_list[i-1][2]
            if (current_org == previous_org):
                row_index = row_index_list[i-1]
            else:
                row_index = (row_index_list[i-1] + 1)%2
            row_index_list.append(row_index)

        return row_index_list