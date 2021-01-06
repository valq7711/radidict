import os, sys
sys.path.append(os.path.normpath(os.path.join(__file__, '../..')))

import unittest
from radidict import RadiDict


def name_filter(route_rest):
    name = route_rest.split('/', 1)[0]
    selector = None
    if name[0] == 'j':
        selector = 1
    elif name[0] == 't':
        selector = 2
    return name, len(name), selector

routes = {
    'a/b/c' : ['a/b/c', None],
    'a1/b1/c1' : ['a1/b1/c1', None],
    'a1/\r/\r' : {
        'data' : 'a1/\r/\r',
        'params' : {
            'b_param' : [False, None],
            'c_param' : [False, None],
        },
        'route_in' : 'a1/b_value/c_value',
        'param_values' : ['b_value', 'c_value']
    },
    'user/\r1/profile' : {
        'data' : 'user/\r1/profile',
        'params' : {
            'name' : [False, name_filter],
        },
        'route_in' : 'user/jim/profile',
        'param_values' : ['jim']
    },
    'user/\r2/profile' : {
        'data' : 'user/\r2/profile',
        'params' : {
            'name' : [False, name_filter],
        },
        'route_in' : 'user/tim/profile',
        'param_values' : ['tim']
    },
    'user/\r/profile' : {
        'data' : 'user/\r/profile',
        'params' : {
            'name' : [False, name_filter],
        },
        'route_in' : 'user/val/profile',
        'param_values' : ['val']
    },
    'user/\r/\r' : {
        'data' : 'user/\r/\r',
        'params' : {
            'name' : [False, name_filter],
            'age' : [False, None],
        },
        'route_in' : 'user/tom/12',
        'param_values' : ['tom', '12']
    },
    'user/\r/\r/some' : {
        'data' : 'user/\r/\r/some',
        'params' : {
            'name' : [False, name_filter],
            'age' : [False, None],
        },
        'route_in' : 'user/tom/12/some',
        'param_values' : ['tom', '12']
    },
    'user/\r/\r/\r' : {
        'data' : 'user/\r/\r/\r',
        'params' : {
            'name' : [False, name_filter],
            'age' : [False, None],
            'other' : [False, None],
        },
        'route_in' : 'user/tom/12/other',
        'param_values' : ['tom', '12', 'other']
    },
}


class TestURL(unittest.TestCase):
    def setUp(self):
        self.rd = RadiDict()
        for r, data_params in routes.items():
            if isinstance(data_params, dict):
                self.rd.add(r, data_params['data'], data_params['params'])
            else:
                self.rd.add(r, *data_params)

    def test_routes(self):
        for r, data_params in routes.items():
            has_param = False
            if isinstance(data_params, dict):
                has_param = True
                rin = data_params['route_in']
            else:
                rin = r
            data, param_names, param_values, hooks = self.rd.get(rin)
            self.assertEqual(data, r)
            if has_param:
                self.assertEqual(param_values, data_params['param_values'])

    def test_hooks(self):
        on_route = 'user/\r'
        hook_data = f'{on_route}-hook' # can be anything
        self.rd.add_hooks(on_route, hook_data, {'name':[False, name_filter]})
        data, param_names, param_values, hooks = self.rd.get('user/tom/profile')
        self.assertEqual(data, 'user/\r2/profile')
        self.assertEqual(param_values, ['tom'])
        self.assertEqual(param_names, ['name'])
        hook_pos = len(on_route.replace('\r', param_values[0]))
        self.assertEqual(hooks, [ [hook_pos, hook_data] ])





if __name__ == "__main__":
    unittest.main()