def main():
    def read_int_list():
        return list(map(int,input().strip().split()))
    
    in_data = read_int_list()
    in_shape = read_int_list()
    kernel_data = read_int_list()
    kernel_shape = read_int_list()
    groups = int(input().strip())

    def solve(in_data,in_shape, kernel_data,kernel_shape,groups):

        if len(in_shape) != 4:
            return ['-1','-1']
        if len(kernel_shape) != 4:
            return ['-1','-1']
        
        batch_size = in_shape[0]
        in_channels = in_shape[1]
        height = in_shape[2]
        width = in_shape[3]

        out_channels = kernel_shape[0]
        k_channels = kernel_shape[1]
        k_h = kernel_shape[2]
        k_w = kernel_shape[3]

        if groups <= 0:
            return ['-1','-1']
        if in_channels % groups != 0:
            return ['-1','-1']
        if out_channels % groups != 0:
            return ['-1','-1']
        
        groups_in_channels = in_channels // groups
        groups_out_channels = out_channels // groups

        if k_channels != groups_in_channels:
            return ['-1','-1']
        
        if k_h > height:
            return ['-1','-1']
        if k_w > width:
            return ['-1','-1']
        
        expected_in_size = batch_size * in_channels * height * width
        expected_kernel_size = out_channels * k_channels * k_h * k_w

        if len(in_data) != expected_in_size:
            return ['-1','-1']
        if len(kernel_data) != expected_kernel_size:
            return ['-1','-1']
        out_h = height - k_h + 1
        out_w = width - k_w + 1

        out_data = []

        def get_input_index(n, ic, h, w):
            return ((n * in_channels + ic) * height + h) * width + w
        def get_kernel_index(oc,kc,kh,kw):
            return ((oc * k_channels + kc) * k_h + kh) * k_w + kw
        for n in range(batch_size):
            for oc in range(out_channels):
                group_id = oc // groups_out_channels
                input_channel_start = group_id * groups_in_channels

                for oh in range(out_h):
                    for ow in range(out_w):
                        total = 0
                        for kc in range(k_channels):
                            ic = input_channel_start + kc

                            for kh in range(k_h):
                                for kw in range(k_w):
                                    input_index = get_input_index(n,ic,oh+kh,ow+kw)
                                    kernel_index = get_kernel_index(oc,kc,kh,kw)

                                    total += in_data[input_index] * kernel_data[kernel_index]

                        out_data.append(total)
        
        out_shape = [batch_size, out_channels, out_h,out_w]
        out_data_line = ' '.join(map(str, out_data))
        out_shape_line = ' '.join(map(str, out_shape))

        return [out_data_line,out_shape_line]
    
    result = solve(in_data,in_shape, kernel_data,kernel_shape, groups)

    for line in result:
        print(line)

if __name__ == '__main__':
    main()
        

