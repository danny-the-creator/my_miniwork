def fused_cubes(cubes):
    result = []
    for j in range(len(cubes)):
        cube = all_cords(cubes[j])
        part_of = None
        ind_del = []
        for i in range(len(result)):
            taken = result[i]
            common_points = {x for xs in taken for x in xs} & {x for xs in cube for x in xs}

            x_cord = {i[0] for i in common_points}
            y_cord = {i[1] for i in common_points}
            z_cord = {i[2] for i in common_points}

            check = len([i for i in [len(x_cord), len(y_cord), len(z_cord)] if i > 1])
            if check > 1:
                if part_of is None:
                    result[i] = taken | cube
                    part_of = i
                else:
                    result[part_of] = result[part_of] | (taken | cube)
                    ind_del.append(i)
        result = [result[i] for i in range(len(result)) if i not in ind_del]
        if part_of is None:
            result.append(cube)
    return [len(i) for i in result]


def all_cords(cube):
    result = set()
    for z in range(cube[3]):
        for y in range(cube[3]):
            for x in range(cube[3]):
                x_cord, y_cord, z_cord = (cube[0]+x, cube[1]+y, cube[2]+z)
                result.add(((x_cord,y_cord,z_cord),(x_cord+1,y_cord,z_cord),(x_cord,y_cord+1,z_cord),
                            (x_cord,y_cord,z_cord+1),(x_cord+1,y_cord+1,z_cord),(x_cord+1,y_cord,z_cord+1),
                            (x_cord,y_cord+1,z_cord+1),(x_cord+1,y_cord+1,z_cord+1),))
    return result
print(len(all_cords((0,0,0,3))))


print(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)]))
print(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)]))
print(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)]))
print(fused_cubes([[0, 0, 0, 3], [-2, -2, -2, 3]]))
print(fused_cubes([[-1,0,0,1],[1,0,0,1],[0,1,0,1],[0,-1,0,1],[0,0,1,1],[0,0,-1,1]]))
print(fused_cubes([[0,0,0,1],[0,1,0,1],[0,2,0,1],[0,3,0,1],[0,5,0,1],[-1,4,0,1],[0,4,0,1],[1,4,0,1],[2,4,0,1],[3,4,0,1],[4,4,0,1],[5,4,0,1],[-1,6,0,1],[0,6,0,1],[1,6,0,1],[2,6,0,1],[3,6,0,1],[4,6,0,1],[5,6,0,1],[4,0,0,1],[4,1,0,1],[4,2,0,1],[4,3,0,1],[4,5,0,1],[2,5,0,1]]))
print(fused_cubes([[-9,0,0,2],[-9,2,0,2],[-5,0,1,2],[-5,2,1,2],[-1,0,2,2],[-1,2,2,2],[3,0,3,2],[3,2,3,2],[7,0,2,2],[7,2,2,2],[6,3,2,2],[4,3,2,2],[2,3,3,2],[0,3,3,2],[-2,3,2,2],[-4,3,2,2],[-2,0,-7,2],[0,0,0,1],[0,1,0,1],[3,0,-1,1],[3,1,-1,1]]))
print(fused_cubes([[-4,0,-4,2],[-2,0,-4,2],[0,0,-4,2],[2,0,-4,2],[2,0,-2,2],[2,0,0,2],[2,0,2,2],[-3,2,-3,2],[-1,2,-3,2],[1,2,-3,2],[1,2,-1,2],[1,2,1,2],[-2,4,-2,2],[0,4,-2,2],[0,4,0,2],[-1,0,-5,1],[0,0,-5,1],[-1,1,-4,2],[-1,3,-3,2],[4,0,-1,1],[4,0,0,1],[2,1,-1,2],[1,3,-1,2],[-1,6,-1,2]]))
